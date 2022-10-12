<script setup lang="ts">
import { Apartment } from '~~/composables/types';
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
import 'swiper/css/navigation'
import 'swiper/css/pagination'
import 'swiper/css/scrollbar'
import LocationIcon from '~~/components/svgs/LocationIcon.vue';
import BedroomIcon from '../../components/svgs/BedroomIcon.vue';
import BathIcon from '../../components/svgs/BathIcon.vue';
import CalenderIcon from '../../components/svgs/CalenderIcon.vue';


const route = useRoute()

const { data: apartmentDetails } = await useFetch<Apartment>(`http://localhost:8000/v1/apartments/${route.params.id}`, { key: `apartments_${route.params.id}` })
const { data: proximityApartments, pending: loadingProximityApartments } = useLazyFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`,
    {
        key: `proximity_apartments_${route.params.id}`,
        params: {
            'location__city': apartmentDetails.value?.location.city,
        }
    }
)
const { data: similarApartments, pending: loadingSimilarApartments } = useLazyFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`,
    {
        key: `similar_apartments_${route.params.id}`,
        params: {
            'apartment_type': apartmentDetails.value?.apartment_type.id,
            'rooms': apartmentDetails.value?.rooms,
        }
    }
)



const modules = [Navigation, Pagination, Scrollbar, A11y]


</script>


<template>
    <div>
        <div class="mx-20 mt-10">
            <div id="apartment-detail-view">
                <main>
                    <div class="swiper-container my-5">
                        <Swiper :modules="modules" navigation :pagination="{ clickable: true }" :centeredSlides="true">
                            <template v-for="image in apartmentDetails.apartment_image">
                                <SwiperSlide id="slide" class="flex justify-center align-center">
                                    <img :src="image.image" :alt="apartmentDetails.name">
                                </SwiperSlide>
                            </template>
                        </Swiper>
                    </div>
                    <div class="my-5">
                        <h2 class="text-xl">{{ apartmentDetails.name }}</h2>
                        <h1 class="text-4xl">GHS {{ apartmentDetails.price }}</h1>
                        <div class="flex items-center mt-2">
                            <LocationIcon />
                            <span class="ml-1">{{ apartmentDetails.location.city }}</span>
                        </div>
                        <div class="flex">
                            <div class="flex items-center">
                                <BedroomIcon />
                                <span class="ml-2">{{ apartmentDetails.bedrooms }} Bedrooms</span>
                            </div>
                            <div class="flex items-center ml-10">
                                <BathIcon />
                                <span class="ml-2">{{ apartmentDetails.bathrooms }} Baths</span>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <CalenderIcon />
                            <span class="ml-2">Available from N/A to N/A</span>
                        </div>
                    </div>

                    <div class="w-full outline outline-1 outline-black opacity-25"></div>

                    <div class="my-10">
                        <h1 class="text-3xl">Features and description</h1>
                        <ul class="columns-2" id="features">
                            <li v-for="feature of apartmentDetails.features">{{ feature.name }}</li>
                        </ul>
                        <p>
                            {{
                            apartmentDetails.description.length ?
                            apartmentDetails.description : 'Listing has no description'
                            }}
                        </p>
                    </div>

                </main>
                <aside>
                    <div class="flex flex-col border p-3 rounded text-center sticky top-20 md:ml-10">
                        <span class="my-2">Contact this Property</span>
                        <button type="button" class="bg-red-200 py-2 my-2">Request Tour</button>
                        <button type="button" class="py-2 my-2 border border-red-200">Send Message</button>
                        <span class="my-2">00 23 434 545</span>
                    </div>
                </aside>
            </div>
            <div>
                <span class="text-2xl py-2">In close proximity</span>
                <template v-if="loadingProximityApartments"></template>
                <template v-else>
                    <CustomCarousel :data="proximityApartments">
                        <template #item="apartment: Apartment">
                            <ApartmentCarouselItem :apartment="apartment" />
                        </template>
                    </CustomCarousel>
                </template>
            </div>
            <div>
                <span class="text-2xl py-2">Similar Apartments</span>
                <template v-if="loadingSimilarApartments"></template>
                <template v-else>
                    <CustomCarousel :data="similarApartments">
                        <template #item="apartment: Apartment">
                            <ApartmentCarouselItem :apartment="apartment" />
                        </template>
                    </CustomCarousel>
                </template>
            </div>
        </div>
    </div>
</template>

<style scoped>
#apartment-detail-view {
    display: grid;
    grid-template-columns: 1fr minmax(150px, 25%);
}

#slide {
    width: 100% !important;
}

:deep(.location-icon),
:deep(.calender-icon),
:deep(.bath-icon),
:deep(.bedroom-icon) {
    width: 25px;
}

#features {
    list-style: disc inside;
}
</style>