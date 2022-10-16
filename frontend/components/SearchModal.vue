<script setup lang="ts">
const dialog = ref<HTMLDialogElement | null>(null)

const { data: apartmentTypes } = fetchApartmentTypes({ lazy: true })

const filters = reactive({
    min_price: "",
    max_price: "",
    rooms: "",
    location__city: "",
    baths: "",
    apartment_type: "",
    search: "",
})

const search = async () => {
    const filtersCopy = filters

    if (filters.rooms == "4") {
        filtersCopy.rooms = ""
        filtersCopy["min_room"] = 4
    }
    if (filters.baths == "4") {
        filtersCopy.baths = ""
        filtersCopy["min_baths"] = 4
    }

    await navigateTo(
        {
            path: '/search/',
            query: filtersCopy
        }
    )
}

</script>

<template>
    <button type="button" @click="dialog.showModal()" class="mr-5">Search</button>
    <Teleport to="body">
        <dialog ref="dialog" class="w-full md:w-[70%] mt-5 rounded-lg h-max-[1000px] w-max-[768px]">
            <form method="dialog" @submit="search()">
                <fieldset class="flex flex-col">
                    <label for="search">Search</label>
                    <input type="search" id="search" placeholder="Enter A City/Region Here"
                        class="w-full h-10 border px-2 rounded" v-model="filters.search" autofocus>
                </fieldset>
                <fieldset class="my-5">
                    <legend class="my-3">Price</legend>
                    <div class="flex flex-col md:block">
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
                    <button type="reset" class="border py-1 px-5" @click="dialog.close()">Cancel</button>
                    <button type="submit" class="ml-3 bg-red-200 py-1 px-5">Search</button>
                </div>
            </form>
        </dialog>
    </Teleport>
</template>

<style scoped>
dialog::backdrop {
    background-color: rgba(0, 0, 0, 0.9);
}
</style>