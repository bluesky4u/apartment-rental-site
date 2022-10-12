<script setup lang="ts">
import { onBeforeRouteUpdate } from 'vue-router';
import { Apartment } from '~~/composables/types';

definePageMeta({
    layout: false
})

const route = useRoute()
const apartments = ref<Apartment[]>([])

const search = async (query: string) => {
    await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { params: { search: query }, key: `apartments?${query}` })
        .then((res) => {
            apartments.value = res.data.value
        })
}

onBeforeRouteUpdate((to, from, next) => {
    if (to.query.searchQuery !== from.query.searchQuery) {
        search(to.query.searchQuery as string)
    }
    next()
})

search(route.query.searchQuery as string)

</script>

<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Showing results for {{route.query.searchQuery}}</h1>
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
