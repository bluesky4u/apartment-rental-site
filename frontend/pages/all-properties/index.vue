<script setup lang="ts">
import { Apartment } from '~~/composables/types';

definePageMeta({
    title: 'All apartments',
    description: 'List of all apartments',
    keywords: 'apartments rentals listings',
    layout: false
})

const { data: apartments } = await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`)
</script>
            
            
<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Browse all listings</h1>
        </template>

        <template v-if="apartments.length">
            <template v-for="apartment of apartments">
                <ApartmentItem :apartment="apartment" />
            </template>
        </template>

        <template #map>
            <Map />
        </template>
    </NuxtLayout>
</template>
        