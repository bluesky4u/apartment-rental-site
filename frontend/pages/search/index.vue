<script setup lang="ts">
import { onBeforeRouteUpdate } from 'vue-router';
import { Apartment } from '~~/composables/types';

definePageMeta({
    layout: false
})

const route = useRoute()
const apartments = ref<Apartment[]>([])

const search = async (query) => {
    await fetchApartments({ params: query, key: `apartments/?search=${query.min_price}-${query.max_price}-${query.rooms}-${query.location__city}-${query.search}-` })
        .then((res) => {
            apartments.value = res.data.value
        })
}

onBeforeRouteUpdate((to, from, next) => {
    if (to.query !== from.query) {
        search(to.query)
    }
    next()
})

search(route.query)

</script>

<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Showing {{ apartments.length }} results</h1>
        </template>
        <template #default>
            <template v-if="apartments.length" v-for="apartment of apartments">
                <ApartmentItem :apartment="apartment" />
            </template>
            <template v-else>
                <p>
                    We are sorry, but we could not find any apartments matching your search query.
                </p>
            </template>
        </template>
        <template #map>
            <Map />
        </template>
    </NuxtLayout>
</template>
