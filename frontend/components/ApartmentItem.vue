<script setup lang="ts">
import { Apartment } from '~~/composables/types';

const props = defineProps<
    {
        apartment: Apartment
    }>()
</script>

<template>
    <div class="border border-grey rounded my-5">
        <div class="flex flex-row w-full">
            <picture class="w-[450px] h-[300px]">
                <NuxtLink :to="`/apartment/${apartment.id}/`">
                    <img :src="apartment.apartment_image[0].image" :alt="`${apartment.name} thumbnail`"
                        class="h-full object-cover w-full">
                </NuxtLink>
            </picture>
            <div class="p-2 w-full flex flex-col justify-between">
                <div>
                    <h2 class="text-xl">GHS {{apartment.price}}</h2>
                    <div class="text-sm text-zinc-500 mb-5">
                        <span>{{apartment.bedrooms}} bedrooms</span> •
                        <span>{{apartment.bathrooms}} bathrooms</span>
                    </div>
                    <p class="font-semibold">{{apartment.name}}</p>
                    <p class="text-zinc-500">{{apartment.location.city}}</p>
                </div>
                <div class="flex flex-row w-full gap-2">
                    <button type="button" class="bg-red-200 px-1 py-2 rounded flex-1">Request
                        Tour</button>
                    <button type="button" class="border border-red-200 rounded flex-1">Send
                        Message</button>
                </div>
            </div>
        </div>
    </div>
</template>