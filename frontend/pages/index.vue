<script setup lang="ts">

import { Apartment, ApartmentType } from '~~/composables/types';

const hero = ref<Element | null>(null)
const navSticky = ref(false)
onMounted(() => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.target == hero.value) {
                if (entry.isIntersecting) {
                    navSticky.value = false
                } else {
                    navSticky.value = true
                }
            }
        })
    }, {
        root: null,
        rootMargin: "0px",
        threshold: 0.8
    })

    observer.observe(hero.value)
})


const [{ data: apartmentTypes }, { data: apartments }] = await Promise.all([fetchApartmentTypes(), fetchApartments()])

definePageMeta({
    layout: false
})
</script>


<template>
    <div id="main">
        <Navbar :hidden="!navSticky" />
        <div ref="hero" class="flex flex-col items-center text-white bg-hero-background bg-center bg-cover py-40"
            id="hero">
            <span class="m-0 text-2xl">Logo</span>
            <h1 class="text-5xl my-4">Find it. Tour it. Make it yours.</h1>
            <SearchBox styleClass="h-10 w-2/5 pl-4" />
        </div>

        <main>
            <section class="mx-20 py-4">
                <h2 class="text-2xl text-center py-3">Explore rentals in Accra</h2>
                <ClientOnly fallbackTag="div">
                    <CustomCarousel :data="apartments">
                        <template #item="apartment: Apartment">
                            <ApartmentCarouselItem :apartment="apartment" />
                        </template>
                    </CustomCarousel>
                    <template #fallback>
                        <div v-for="apartment of apartments">
                            <h2>{{apartment.name}}</h2>
                            <img :src="apartment.apartment_image[0].image" :alt="`${apartment.name} image`" style="height: 50px">
                            <p>{{apartment.price}}</p>
                            <p>{{apartment.location.city}}</p>
                        </div>
                    </template>
                </ClientOnly>

            </section>

            <section class="mx-20 py-4">
                <h2 class="text-2xl text-center py-3">Browse apartments by type</h2>
                <ClientOnly fallbackTag="div">
                    <CustomCarousel :data="apartmentTypes">
                        <template #item="apartment_type: ApartmentType">
                            <div class="flex flex-col items-center mb-10">
                                <NuxtLink :to="`/type/${apartment_type.id}`">
                                    <div><img :src="apartment_type.image" :alt="apartment_type.name"
                                            class="md:h-[15rem] h-[10rem] object-cover object-center"></div>
                                    <div class="pt-2">
                                        <span class="text-xl">{{ apartment_type.name }}</span>
                                    </div>
                                </NuxtLink>
                            </div>
                        </template>
                    </CustomCarousel>
                    <template #fallback>
                        <div v-for="apartmentType of apartmentTypes">
                            <h2>{{apartmentType.name}}</h2>
                            <img :src="apartmentType.image" :alt="`${apartmentType.name} image`">
                        </div>
                    </template>
                </ClientOnly>
            </section>

            <section class="text-center bg-hero-background py-40 bg-center bg-cover text-white">
                <h2 class="text-3xl mb-16">Let's help you find your new home</h2>
                <NuxtLink to="/all-properties/" class="border border-blue-500 text-blue-500 px-5 py-2 rounded">Explore
                    all properties</NuxtLink>
            </section>

            <section class="mx-20 my-5">
                <div>
                    <div class="flex flex-row items-center">
                        <span class="text-xl flex-none pr-5">Who are we</span>
                        <span class="after:content-[''] flex-1 box-border h-px border-t border-black"></span>
                    </div>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi vel quia tempore sint repellat
                        dolor ipsa. Rem dolores perspiciatis ea itaque? Error tenetur rem facilis voluptatum molestias
                        laboriosam reiciendis, eius officia amet possimus beatae natus reprehenderit explicabo modi
                        laborum consequatur, sed nemo! Aperiam illum quas minima dolores suscipit expedita, explicabo
                        quasi rerum, excepturi adipisci dolore molestiae! Sint odio accusantium deserunt et rem
                        voluptatum veniam distinctio aut ratione eligendi vel quas maxime at repellendus quos, quaerat
                        ipsam consequuntur illo sunt quis! Eveniet est quibusdam, consectetur facere tempora, molestiae
                        magni saepe dolor optio totam voluptate voluptatibus facilis obcaecati. Voluptatibus laborum
                        voluptatem natus!</p>
                </div>
                <div>
                    <div class="flex flex-row items-center">
                        <span class="text-xl flex-none pr-5">Who are we</span>
                        <span class="after:content-[''] flex-1 box-border h-px border-t border-black"></span>
                    </div>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi vel quia tempore sint repellat
                        dolor ipsa. Rem dolores perspiciatis ea itaque? Error tenetur rem facilis voluptatum molestias
                        laboriosam reiciendis, eius officia amet possimus beatae natus reprehenderit explicabo modi
                        laborum consequatur, sed nemo! Aperiam illum quas minima dolores suscipit expedita, explicabo
                        quasi rerum, excepturi adipisci dolore molestiae! Sint odio accusantium deserunt et rem
                        voluptatum veniam distinctio aut ratione eligendi vel quas maxime at repellendus quos, quaerat
                        ipsam consequuntur illo sunt quis! Eveniet est quibusdam, consectetur facere tempora, molestiae
                        magni saepe dolor optio totam voluptate voluptatibus facilis obcaecati. Voluptatibus laborum
                        voluptatem natus!</p>
                </div>
            </section>
        </main>
        <Footer />
    </div>
</template>
