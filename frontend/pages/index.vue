<script setup lang="ts">
interface Apartment {
    id: number;
    name: string;
    location: ApartmentLocation;
    price: number;
    bedrooms: number;
    bathrooms: number;
    description: string;
    image?: string;
    availability?: Date
}

interface ApartmentLocation {
    id: number;
    city: string;
    long: number;
    lat: number;
}

interface ApartmentType {
    id: number;
    name: string;
}
const { data } = await useFetch<Apartment[]>('http://127.0.0.1:8000/v1/apartments')
</script>


<template>
    <div id="main">
        <header class="flex flex-col items-center text-white">
            <h1 class="m-0 text-2xl">Logo</h1>
            <h1 class="text-5xl my-4">Find it. Tour it. Make it yours.</h1>
            <label for="search" class="hidden">Search</label>
            <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4" placeholder="Enter A City/Region Here">
        </header>

        <main>
            <h2 class="text-2xl text-center">Explore rentals in Accra</h2>
        </main>
    </div>
</template>

<style scoped>
header {
    background: linear-gradient(rgba(0, 0, 0, 0.55),
            rgba(0, 0, 0, 0.55)), url(~/assets/img/estate.jpg);
    background-size: cover;
    background-position: center;
    mix-blend-mode: color-dodge;
    padding: 10rem 0;
}
</style>