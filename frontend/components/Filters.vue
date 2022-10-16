<script setup lang="ts">
import { Apartment } from '~~/composables/types';

const emits = defineEmits<{ (e: 'updateApartmentList', apartment: Apartment[]): void }>()

const { data: apartmentTypes } = fetchApartmentTypes({ lazy: true })

const params = reactive({
    max_price: "",
    rooms: ""
})

const filters = reactive({
    min_price: "",
    max_price: "",
    rooms: "",
    location__city: "",
    baths: "",
    apartment_type: ""
})

watch(params, async (value) => {
    if (value.rooms == "4") {
        await fetchApartments({ key: `apartments-max-price-${params.max_price}-rooms-${params.rooms}`, params: { "max_price": params.max_price, "min_room": 4 } })
            .then(res => {
                emits("updateApartmentList", res.data.value)
            })
    } else {
        await fetchApartments({ key: `apartments-max-price-${params.max_price}-rooms-${params.rooms}`, params: params })
            .then(res => emits("updateApartmentList", res.data.value))
    }
})


const modal = ref<HTMLDialogElement | null>(null)
const filterResults = async () => {
    const filtersCopy = filters
    if (filters.rooms == "4") {
        filtersCopy.rooms = ""
        filtersCopy["min_room"] = 4
    }
    if (filters.baths == "4") {
        filtersCopy.baths = ""
        filtersCopy["min_baths"] = 4
    }

    await fetchApartments({ lazy: true, params: filtersCopy, key: `apartments-${Math.random() * 100}` })
        .then(res => { emits("updateApartmentList", res.data.value) })
}

</script>

<template>
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

        <button type="button" class="border ml-2 px-2" @click="modal.showModal()">More</button>

        <Teleport to="body">
            <dialog ref="modal" class="px-21">
                <div class="flex flex-row justify-between">
                    <span>Filters</span>
                    <button type="button" @click="modal.close()">X</button>
                </div>
                <form method="dialog" @submit="filterResults()">
                    <fieldset class="my-5">
                        <legend class="my-3">Price</legend>
                        <div>
                            <input type="number" name="min-price" id="min-price" v-model="filters.min_price"
                                class="border mr-5 pl-3 py-3" placeholder="Minimum">
                            <span class="mr-5">to</span>
                            <input type="number" name="max-price" id="max-price" v-model="filters.max_price"
                                class="border mr-5 pl-3 py-3" placeholder="Maximum">
                        </div>
                    </fieldset>
                    <fieldset class="flex flex-row my-5">
                        <div class="flex flex-col">
                            <label for="beds-filter" class="my-3">Beds</label>
                            <select name="beds-filter" id="beds-filter" class="border mr-5 pl-3 py-3"
                                v-model="filters.rooms">
                                <option value="">All</option>
                                <option v-for="i of [1,2,3]" :value="i">{{`${i} ${i == 1 ? 'Bed' : 'Beds'}`}}
                                </option>
                                <option value="4">4+ Beds</option>
                            </select>
                        </div>
                        <div class="flex flex-col">
                            <label for="baths" class="my-3">Baths</label>
                            <select name="baths" id="baths" class="border mr-5 pl-3 py-3" v-model="filters.baths">
                                <option value="">All</option>
                                <option v-for="i of [1,2,3]" :value="i">{{`${i} ${i == 1 ? 'Bath' : 'Baths'}`}}
                                </option>
                                <option value="4">4+ Baths</option>
                            </select>
                        </div>
                    </fieldset>
                    <fieldset class="my-5 flex flex-col">
                        <legend class="my-3">Type</legend>
                        <select name="apartment-type" id="apartment-type" class="border mr-5 pl-3 py-3"
                            v-model="filters.apartment_type">
                            <option value="">All</option>
                            <option v-for="apartmentType of apartmentTypes" :value="apartmentType.id">
                                {{apartmentType.name}}
                            </option>
                        </select>
                    </fieldset>
                    <div class="flex justify-end">
                        <button type="reset" class="border py-1 px-5">Reset</button>
                        <button type="submit" class="ml-3 bg-red-200 py-1 px-5">Filter</button>
                    </div>
                </form>
            </dialog>
        </Teleport>
    </div>
</template>

<style scoped>
dialog {
    z-index: 9999;
    width: 80%;
    max-width: 784px;
    max-height: 100vh;
}

dialog::backdrop {
    background: #000;
    opacity: 0.8;
}
</style>
