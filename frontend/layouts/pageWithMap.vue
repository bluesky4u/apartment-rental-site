<template>
    <div>
        <Navbar />
        <div class="mx-5 flex relative">
            <div class="w-full md:flex-[0_0_600px] min-h-full overflow-y-auto">
                <slot name="heading"></slot>
                <slot name="default"></slot>
                <Footer />
            </div>
            <div class="fixed map hidden md:block">
                <slot name="map"></slot>
            </div>
        </div>

    </div>
</template>

<style scoped>
.map {
    width: calc(100% - 630px);
    top: 80px;
    right: 0px;
}
</style>