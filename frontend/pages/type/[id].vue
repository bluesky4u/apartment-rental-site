<script setup lang="ts">
import { Apartment, ApartmentImage } from '~~/composables/types';
import DataView from 'primevue/dataview';

const route = useRoute()

const apartments: Apartment[] = [
    {
        id: 1,
        name: 'Apartment 1',
        location: {
            id: 1,
            city: 'City 1',
            long: 0,
            lat: 0,
        },
        price: 100,
        bedrooms: 1,
        bathrooms: 1,
        description: 'Description 1',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300',
            }
        ],
    },
    {
        id: 2,
        name: 'Apartment 2',
        location: {
            id: 2,
            city: 'City 2',
            long: 0,
            lat: 0,
        },
        price: 200,
        bedrooms: 2,
        bathrooms: 2,
        description: 'Description 2',
        image: [
            {
                id: 2,
                image: 'https://picsum.photos/200/300',
            }
        ],
    },
    {
        id: 3,
        name: 'Apartment 3',
        location: {
            id: 3,
            city: 'City 3',
            long: 0,
            lat: 0,
        },
        price: 300,
        bedrooms: 3,
        bathrooms: 3,
        description: 'Description 3',
        image: [
            {
                id: 3,
                image: 'https://picsum.photos/200/300',
            }
        ],
    },
    {
        id: 4,
        name: 'Apartment 4',
        location: {
            id: 4,
            city: 'City 4',
            long: 0,
            lat: 0,
        },
        price: 400,
        bedrooms: 4,
        bathrooms: 4,
        description: 'Description 4',
        image: [
            {
                id: 4,
                image: 'https://picsum.photos/200/300'
            }
        ]
    }
]

</script>
    
    
<template>
    <div class="min-h-screen">
        <Navbar />
        <div class="mx-20">
            <h1>All Condos</h1>
            <DataView :value="apartments" data-key="id">
                <template #list="slotProps">
                    <div class="grid grid-cols-12">
                        <img :src="slotProps.data.image[0].image" class="w-full aspect-square">
                        <div class="flex flex-col col-start-2 col-end-13">
                            <h1>{{ slotProps.data.name }}</h1>
                            <h2>{{ slotProps.data.location.city }}</h2>
                            <h3>{{ slotProps.data.price }}</h3>
                        </div>
                    </div>
                </template>
            </DataView>
        </div>
    </div>
</template>
    
<style scoped>
#apartment-detail-view {
    display: grid;
    grid-template-columns: 1fr minmax(150px, 25%);
}

#slide {
    width: 100% !important;
}

:deep(.location-icon),
:deep(.calender-icon),
:deep(.bath-icon),
:deep(.bedroom-icon) {
    width: 25px;
}

#features {
    list-style: disc inside;
}
</style>