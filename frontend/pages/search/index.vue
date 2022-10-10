<script setup lang="ts">
import { Apartment } from '~~/composables/types';

definePageMeta({
    layout: false
})

const route = useRoute()

const { data: apartments } = await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { params: { search: route.query.searchQuery } })
</script>

<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Showing results for {{route.query.searchQuery}}</h1>
        </template>
        <template #default>
            <template v-for="apartment of apartments">
                <ApartmentItem :apartment="apartment" />
            </template>
        </template>
        <template #map>
            <Map />
        </template>
    </NuxtLayout>
</template>
