<template>
    <footer class="mx-20 my-10 flex flex-row justify-between">
        <div class="flex flex-col w-1/2">
            <span class="text-2xl">Logo</span>
            <span>About us</span>
            <span>Contact us</span>

        </div>
        <div class="w-1/2 flex flex-col">
            <span>On a hunt? We can send you updates</span>
            <div class="flex flex-row my-5 justify-between">
                <label for="email" class="hidden">Search</label>
                <input type="email" id="email" class="h-10 w-4/5 mr-2 bg-[#374151] pl-4 rounded-full text-white"
                    placeholder="Email Address">
                <button type="button" class="border-blue-500 border px-3 rounded">Submit</button>
            </div>
        </div>
    </footer>
</template>