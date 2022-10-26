<script setup lang="ts">
import { Apartment } from '~~/composables/types';

definePageMeta({
    title: 'All apartments',
    description: 'List of all apartments',
    keywords: 'apartments rentals listings',
    layout: false
})


const { data: apartments } = await fetchApartments({ key: `apartments` })
const updateApartments = (newApartments: Apartment[]) => apartments.value = newApartments
</script>
            
            
<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Browse all listings</h1>
            <Filters @update-apartment-list="updateApartments" />
        </template>

        <template v-for="apartment of apartments">
            <ApartmentItem :apartment="apartment" />
        </template>

        <template #map>
            <Map />
        </template>
    </NuxtLayout>
</template>
        