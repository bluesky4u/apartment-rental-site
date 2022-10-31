<script setup lang="ts">
definePageMeta(
    {
        title: 'Admin'
    }
)

useHead(
    {
        meta: [
            { name: 'robots', content: 'noindex' }
        ],
    }
)

await navigateTo(`${baseURL}/admin`, { external: true })
</script>

<template>
</template>