<script setup lang="ts">
import { Apartment } from '~~/composables/types';

const route = useRoute()

definePageMeta({
    title: 'Apartment Details',
    description: 'Apartment Details',
    keywords: 'Apartment Details',
    layout: false
})


const { data: apartments } = await fetchApartments({ key: `apartment_type_${route.params.id}`, params: { 'apartment_type': route.params.id } })
</script>
    
    
<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Browse all listings in the {{ apartments.length ?
                    apartments[0].apartment_type.name : 'this'
            }} category</h1>
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
