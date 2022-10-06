<template>
    <nav ref="nav" class="flex flex-row justify-between items-center sticky inset-x-0 top-0 py-5 z-50 bg-white">
        <span class="m-0 pl-5 text-2xl">
            <NuxtLink to="/">Logo</NuxtLink>
        </span>
        <label for="search" class="hidden">Search</label>
        <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4" placeholder="Enter A City/Region Here">
    </nav>
</template>