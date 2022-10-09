<script setup lang="ts">
import { Apartment } from '~~/composables/types';

const route = useRoute()

definePageMeta({
    title: 'Apartment Details',
    description: 'Apartment Details',
    keywords: 'Apartment Details',
    layout: false
})


const { data: apartments } = await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartment_type_${route.params.id}`, params: { 'apartment_type': route.params.id } })
</script>
    
    
<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Browse all listings in the {{apartments.length ?
            apartments[0].apartment_type.name: 'this'}} category</h1>
        </template>

        <template v-if="apartments.length">
            <template v-for="apartment of apartments">
                <div class="border border-grey rounded my-5">
                    <div class="flex flex-row w-full">
                        <picture class="max-w-[320px] h-[300px]">
                            <NuxtLink :to="`/apartment/${apartment.id}/`">
                                <img :src="apartment.apartment_image[0].image" :alt="`${apartment.name} thumbnail`"
                                    class="h-full object-cover">
                            </NuxtLink>
                        </picture>
                        <div class="p-2 w-full flex flex-col justify-between">
                            <div>
                                <h2 class="text-xl">GHS {{apartment.price}}</h2>
                                <div class="text-sm text-zinc-500 mb-5">
                                    <span>{{apartment.bedrooms}} bedrooms</span> •
                                    <span>{{apartment.bathrooms}} bathrooms</span>
                                </div>
                                <p class="font-semibold">{{apartment.name}}</p>
                                <p class="text-zinc-500">{{apartment.location.city}}</p>
                            </div>
                            <div class="flex flex-row w-full gap-2">
                                <button type="button" class="bg-red-200 px-1 py-2 rounded flex-1">Request
                                    Tour</button>
                                <button type="button" class="border border-red-200 rounded flex-1">Send
                                    Message</button>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </template>

        <template #map>
                <Map />
        </template>
    </NuxtLayout>
</template>
