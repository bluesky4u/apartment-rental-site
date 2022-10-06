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


const apartments = ref<Apartment[]>([])

const { data } = await useFetch<Apartment[]>('http://127.0.0.1:8000/v1/apartments')
apartments.value = data.value

</script>


<template>
    <div id="main" ref="main">
        <header class="flex flex-col w-full" ref="header">
            <nav ref="nav" class="flex flex-row justify-between items-center fixed inset-x-0 top-0 py-5 z-50"
                :class="navSticky ? 'bg-white' : 'bg-transparent'">
                <span class="m-0 pl-5 text-2xl">
                    <NuxtLink to="/">Logo</NuxtLink>
                </span>
                <label for="search" class="hidden">Search</label>
                <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4"
                    placeholder="Enter A City/Region Here">

            </nav>
            <div ref="hero" class="flex flex-col items-center text-white bg-hero-background bg-center bg-cover py-40">
                <span class="m-0 text-2xl">Logo</span>
                <h1 class="text-5xl my-4">Find it. Tour it. Make it yours.</h1>
                <label for="search" class="hidden">Search</label>
                <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4"
                    placeholder="Enter A City/Region Here">
            </div>
        </header>

        <main>
            <section class="mx-20 py-4">
                <h2 class="text-2xl text-center py-3">Explore rentals in Accra</h2>
                <ClientOnly fallbackTag="div">
                    <CustomCarousel :data="apartments">
                        <template #item="apartment: Apartment">
                            <div class="flex flex-col items-center mb-10">
                                <NuxtLink :to="`/apartment/${apartment.id}`">
                                    <div>
                                        <img :src="apartment.apartment_image ? apartment.apartment_image[0].image : `https://picsum.photos/200/300`"
                                            alt="Apartment" class="apartment-image">
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
                    <template #fallback>
                        <div v-for="apartment of apartments">
                            <h2>{{apartment.name}}</h2>
                            <img :src="apartment.apartment_image[0].image" :alt="`${apartment.name} image`">
                            <p>{{apartment.price}}</p>
                            <p>{{apartment.location.city}}</p>
                        </div>
                    </template>
                </ClientOnly>

            </section>

            <section class="mx-20 py-4">
                <h2 class="text-2xl text-center py-3">Browse apartments by type</h2>
                <!-- <CustomCarousel :data="apartmentTypes">
                    <template #item="apartment_type: ApartmentType">
                        <div class="flex flex-col items-center mb-10">
                            <NuxtLink :to="`type/${1}`">
                                <div><img :src="apartment_type.image" :alt="apartment_type.name"></div>
                                <div class="pt-2">
                                    <span class="text-xl">{{ apartment_type.name }}</span>
                                </div>
                            </NuxtLink>
                        </div>
                    </template>
                </CustomCarousel> -->
            </section>

            <section class="text-center bg-hero-background py-40 bg-center bg-cover text-white">
                <h2 class="text-3xl mb-16">Let's help you find your new home</h2>
                <Button label="Explore all properties" class=" p-button-rounded  p-button-outlined" @click="" />
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

    </div>
</template>
