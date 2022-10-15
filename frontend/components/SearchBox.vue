<script setup lang="ts">

interface Props {
    styleClass?: string
}

withDefaults(defineProps<Props>(), {
    styleClass: "h-10 w-2/5",
})

const searchField = ref<string>("")

const search = async () => {
    await navigateTo(
        {
            path: '/search',
            query:
            {
                searchQuery: searchField.value
            }
        })
}
</script>

<template>
    <form @submit.prevent="search" :class="styleClass" class="flex bg-[#374151] text-white">
        <label for="search" class="hidden">Search</label>
        <input type="search" id="search" placeholder="Enter A City/Region Here"
            class="bg-[#374151] w-full focus-within:outline-none focus-visible:outline-none pl-4 h-full"
            v-model="searchField">
        <input v-if="searchField.length" type="submit" value="Search" class="px-3">
    </form>
</template>
