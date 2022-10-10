<script setup lang="ts">

interface Props {
    hidden?: boolean
}

withDefaults(defineProps<Props>(), {
    hidden: false
})

const searchField = ref<string>("")

const search = async (searchQuery: string) => {
    await navigateTo(
        {
            path: '/search',
            query:
            {
                searchQuery: searchQuery
            }
        })
}

</script>

<template>
    <nav class="flex flex-row justify-between items-center sticky inset-x-0 top-0 py-5 z-50 bg-white"
        :class="{'hidden': hidden}">
        <span class="m-0 pl-5 text-2xl">
            <NuxtLink to="/">Logo</NuxtLink>
        </span>
        <label for="search" class="hidden">Search</label>
        <form @submit.prevent="search(searchField)" class="h-10 w-2/5">
            <input type="search" id="search" placeholder="Enter A City/Region Here"
                class="bg-[#374151] w-full pl-4 h-full" v-model="searchField">
        </form>
    </nav>
</template>