<script setup lang="ts">
import { onBeforeRouteUpdate } from 'vue-router';

definePageMeta({
    layout: false
})

const route = useRoute()
const { data: apartments } = await searchApartments(route.query)

const search = async (query) => {

}

onBeforeRouteUpdate(async (to, from, next) => {
    if (to.query !== from.query) {
        await searchApartments(to.query)
            .then((res) => {
                apartments.value = res.data.value
            })
    }
    next()
})


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
