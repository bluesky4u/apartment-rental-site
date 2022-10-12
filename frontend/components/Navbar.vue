<script setup lang="ts">

interface Props {
    hidden?: boolean
}

withDefaults(defineProps<Props>(), {
    hidden: false
})

</script>

<template>
    <nav class="flex flex-row justify-between items-center sticky inset-x-0 top-0 py-5 z-50 bg-white"
        :class="{'hidden': hidden}">
        <span class="m-0 pl-5 text-2xl">
            <NuxtLink to="/">Logo</NuxtLink>
        </span>
        <SearchBox />
    </nav>
</template>