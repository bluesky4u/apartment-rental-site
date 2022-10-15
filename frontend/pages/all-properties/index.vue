<script setup lang="ts">
import { Apartment } from '~~/composables/types';

definePageMeta({
    title: 'All apartments',
    description: 'List of all apartments',
    keywords: 'apartments rentals listings',
    layout: false
})


const params = reactive({
    max_price: "",
    rooms: ""
})

const { data: apartments } = useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments`, params: params })

watch(params, async (value) => {
    if (value.rooms == "4") {
        await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments-max-price-${params.max_price}-rooms-${params.rooms}`, params: { "max_price": params.max_price, "min_room": 4 } })
            .then(res => {
                apartments.value = res.data.value
            })
    } else {
        await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments-max-price-${params.max_price}-rooms-${params.rooms}`, params: params })
            .then(res => apartments.value = res.data.value)
    }
})


await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments` })
    .then(res => {
        apartments.value = res.data.value
    })

const maxPrice = ref("")
watch(maxPrice, async value => {
    await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments-max-price-${value}`, params: { 'max_price': value } })
        .then(res => {
            apartments.value = res.data.value
        })
})

const beds = ref("")
watch(beds, async value => {
    if (value == "4") {
        await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments-beds-${value}`, params: { 'min_room': value } })
            .then(res => {
                apartments.value = res.data.value
            })
    } else {
        await useFetch<Apartment[]>(`http://localhost:8000/v1/apartments/`, { key: `apartments-beds-${value}`, params: { 'bedrooms': value } })
            .then(res => {
                apartments.value = res.data.value
            })
    }
})
</script>
            
            
<template>
    <NuxtLayout name="page-with-map">
        <template #heading>
            <h1 class="text-xl font-semibold">Browse all listings</h1>
            <div class="flex flex-row">
                <SearchBox style-class="w-full py-3 rounded" />

                <label for="beds" class="hidden">Beds</label>
                <select name="beds" id="beds" class="border px-2 ml-2" v-model="params.rooms">
                    <option value="">Beds</option>
                    <option v-for="i of [1,2,3]" :value="i">{{`${i} ${i == 1 ? 'Bed' : 'Beds'}`}}</option>
                    <option value="4">4+ Beds</option>
                </select>

                <label for="max-price" class="hidden">Max Price</label>
                <select name="max-price" id="max-price" class="border px-2 ml-2" v-model="params.max_price">
                    <option value="">Max Price</option>
                    <option value="1000">GHS 1000.00</option>
                    <option value="2000">GHS 2000.00</option>
                    <option value="5000">GHS 5000.00</option>
                    <option value="10000">GHS 10000.00</option>
                </select>

                <button type="button" class="border ml-2 px-2">More</button>
            </div>
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
        