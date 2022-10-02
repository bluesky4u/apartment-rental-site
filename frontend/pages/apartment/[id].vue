<script setup lang="ts">
import { Apartment, ApartmentImage } from '~~/composables/types';
import { Navigation, Pagination, Scrollbar, A11y, Autoplay } from 'swiper';
import 'swiper/css/navigation'
import 'swiper/css/pagination'
import 'swiper/css/scrollbar'
import LocationIcon from '~~/components/svgs/LocationIcon.vue';
import BedroomIcon from '../../components/svgs/BedroomIcon.vue';
import BathIcon from '../../components/svgs/BathIcon.vue';
import CalenderIcon from '../../components/svgs/CalenderIcon.vue';


const route = useRoute()

const apartmentDetails: Apartment = {
    id: 0,
    name: route.fullPath,
    location: {
        city: "Kasoa",
        id: 1,
        lat: 2,
        long: 3
    },
    price: 4999.99,
    bedrooms: 3,
    bathrooms: 2,
    description: '',
    image: [
        { id: 1, image: "https://picsum.photos/900/500" },
        { id: 2, image: "https://picsum.photos/200/300" },
        { id: 3, image: "https://picsum.photos/200/300" },
        { id: 4, image: "https://picsum.photos/200/300" },
        { id: 5, image: "https://picsum.photos/200/300" },
    ]
}


const proximityApartments: Apartment[] = [
    {
        id: 1,
        name: 'Apartment 1',
        location: {
            id: 1,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 100,
        bedrooms: 2,
        bathrooms: 2,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 2,
        name: 'Apartment 2',
        location: {
            id: 2,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 200,
        bedrooms: 3,
        bathrooms: 3,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 3,
        name: 'Apartment 3',
        location: {
            id: 3,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 300,
        bedrooms: 4,
        bathrooms: 4,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 4,
        name: 'Apartment 4',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 5,
        name: 'Apartment 5',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 6,
        name: 'Apartment 6',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
]

const features = ["School", "Bathroom", "A whole", "inside bar", "alley"]
const modules = [Navigation, Pagination, Scrollbar, A11y, Autoplay]

</script>


<template>
    <div>
        <Navbar />
        <div class="mx-20 mt-10">
            <div id="apartment-detail-view">
                <main>
                    <div class="swiper-container my-5">
                        <Swiper :modules="modules" navigation :pagination="{ clickable: true }" :centeredSlides="true">
                            <template v-for="image in apartmentDetails.image">
                                <SwiperSlide id="slide" class="flex justify-center align-center">
                                    <img :src="image.image" :alt="apartmentDetails.name">
                                </SwiperSlide>
                            </template>
                        </Swiper>
                    </div>
                    <div class="my-5">
                        <h2 class="text-xl">{{ apartmentDetails.name }}</h2>
                        <h1 class="text-4xl">{{ apartmentDetails.price }} GHS</h1>
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
                            <li v-for="feature of features">{{ feature }}</li>
                        </ul>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia ut quia eum optio placeat
                            voluptate nostrum sequi, sapiente exercitationem atque illo dolorum labore at est maxime
                            nemo eius pariatur totam facere cum dolorem, dicta nesciunt laboriosam. Animi repellendus
                            quas quasi voluptates, sequi impedit sint consectetur laborum deleniti quis quaerat
                            consequuntur? Nemo perspiciatis eius iure a molestias quas rerum odit, repellat eum optio
                            voluptates aut alias ipsum, fuga blanditiis impedit? Sunt error illo officiis consequuntur
                            at nostrum vel, optio nobis consequatur, quos perferendis? Iusto repellendus provident
                            architecto harum fugiat voluptatem modi quibusdam rerum necessitatibus minus itaque a, porro
                            eveniet ex, amet nihil. Quam suscipit repellendus temporibus a repudiandae mollitia hic
                            aliquid sapiente voluptatibus facere earum praesentium officiis libero, esse ipsam dolorem
                            soluta quos architecto est natus necessitatibus saepe! Ratione quas laudantium illo dolorum
                            possimus veritatis exercitationem repudiandae iste eum quaerat natus corrupti, id commodi
                            consequuntur sed facilis eaque nisi quam accusantium modi recusandae, esse deserunt? Ratione
                            dolor eius omnis neque repudiandae. Ullam repellendus, similique, a neque laudantium ducimus
                            ipsa veritatis facilis temporibus adipisci perferendis ea cumque, quod reprehenderit aliquid
                            repudiandae ipsum cupiditate? Debitis vel perspiciatis nam corporis. Eligendi eum ipsum
                            dolores impedit, eius voluptas modi quos nisi officia minima. Minus provident fugiat
                            repellendus pariatur, culpa doloribus cumque est, architecto expedita quibusdam fuga sed,
                            tenetur nemo amet ratione odio quidem dicta porro quas ea tempore illo incidunt.
                            Consequuntur tempora ex quae, unde voluptas quod itaque est sequi obcaecati dolorem aut nam
                            optio dignissimos temporibus, maiores ad praesentium. Tempora esse beatae repellat id.</p>
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
                <CustomCarousel :data="proximityApartments">
                    <template #item="apartment: Apartment">
                        <div class="flex flex-col items-center mb-10">
                            <NuxtLink :to="`/apartment/` + apartment.id">
                                <div>
                                    <img :src="apartment.image[0].image" alt="Apartment" class="apartment-image">
                                </div>
                                <div class="pt-2">
                                    <span class="text-xl">{{ apartment.name }}</span>
                                    <p class="">{{ apartment.location.city }}</p>
                                    <p class="">{{ apartment.price }}</p>
                                </div>
                            </NuxtLink>
                        </div>
                    </template>
                </CustomCarousel>
            </div>
            <div>
                <span class="text-2xl py-2">Similar Apartments</span>
                <CustomCarousel :data="proximityApartments">
                    <template #item="apartment: Apartment">
                        <div class="flex flex-col items-center mb-10">
                            <NuxtLink :to="`/apartment/` + apartment.id">
                                <div>
                                    <img :src="apartment.image[0].image" alt="Apartment" class="apartment-image">
                                </div>
                                <div class="pt-2">
                                    <span class="text-xl">{{ apartment.name }}</span>
                                    <p class="">{{ apartment.location.city }}</p>
                                    <p class="">{{ apartment.price }}</p>
                                </div>
                            </NuxtLink>
                        </div>
                    </template>
                </CustomCarousel>
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