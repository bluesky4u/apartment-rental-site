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
    <form @submit.prevent="search" :class="styleClass">
        <label for="search" class="hidden">Search</label>
        <input type="search" id="search" placeholder="Enter A City/Region Here" class="bg-[#374151] w-full pl-4 h-full"
            v-model="searchField">
    </form>
</template>
