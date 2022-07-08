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
    <div>
        <ul>
            <li v-for="apartment in data">
                {{ apartment.name }}
            </li>
        </ul>
    </div>
</template>