<script setup lang="ts">
interface Apartment {
    id: number;
    name: string;
    location: ApartmentLocation;
    price: number;
    bedrooms: number;
    bathrooms: number;
    description: string;
    image: ApartmentImage[];
    availability?: Date
}

interface ApartmentLocation {
    id: number;
    city: string;
    long: number;
    lat: number;
}

interface ApartmentType {
    id: number;
    name: string;
    image: string;
}

interface ApartmentImage {
    id: number;
    image: string;
}


const hero = ref<Element | null>(null)
const navSticky = ref(false)
onMounted(() => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.target == hero.value) {
                if (entry.isIntersecting) {
                    navSticky.value = false
                } else {
                    navSticky.value = true
                }
            }
        })
    }, {
        root: null,
        rootMargin: "0px",
        threshold: 0.8
    })

    observer.observe(hero.value)
})


const apartments: Apartment[] = [
    {
        id: 1,
        name: 'Apartment 1',
        location: {
            id: 1,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 100,
        bedrooms: 2,
        bathrooms: 2,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 2,
        name: 'Apartment 2',
        location: {
            id: 2,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 200,
        bedrooms: 3,
        bathrooms: 3,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 3,
        name: 'Apartment 3',
        location: {
            id: 3,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 300,
        bedrooms: 4,
        bathrooms: 4,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 4,
        name: 'Apartment 4',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 5,
        name: 'Apartment 5',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 6,
        name: 'Apartment 6',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 7,
        name: 'Apartment 7',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 8,
        name: 'Apartment 8',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 9,
        name: 'Apartment 9',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
    {
        id: 10,
        name: 'Apartment 10',
        location: {
            id: 4,
            city: 'New York',
            long: -73.935242,
            lat: 40.730610
        },
        price: 400,
        bedrooms: 5,
        bathrooms: 5,
        description: 'This is a description',
        image: [
            {
                id: 1,
                image: 'https://picsum.photos/200/300'
            },
            {
                id: 2,
                image: 'https://picsum.photos/200/300'
            }
        ],
        availability: new Date()
    },
]

const apartmentTypes: ApartmentType[] = [
    {
        id: 1,
        name: "Condo",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 2,
        name: "Villas",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 3,
        name: "Townhouse",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 4,
        name: "Apartment",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 5,
        name: "House",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 6,
        name: "Studio",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 7,
        name: "Loft",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 8,
        name: "Bed & Breakfast",
        image: "https://picsum.photos/200/300"
    },
    {
        id: 9,
        name: "Boat",
        image: "https://picsum.photos/200/300"
    }
]

const responsiveOptions = [
    {
        breakpoint: '1024px',
        numVisible: 3,
        numScroll: 3
    },
    {
        breakpoint: '600px',
        numVisible: 2,
        numScroll: 2
    },
    {
        breakpoint: '480px',
        numVisible: 1,
        numScroll: 1
    }
]

const { data } = await useFetch<Apartment[]>('http://127.0.0.1:8000/v1/apartments')
</script>


<template>
    <div id="main" ref="main">
        <header class="flex flex-col w-full" ref="header">
            <nav ref="nav" class="flex flex-row justify-between items-center fixed inset-x-0 top-0 py-5 z-50"
                :class="navSticky ? 'bg-gray-900' : 'bg-transparent'">
                <span class="m-0 text-2xl">Logo</span>
                <label for="search" class="hidden">Search</label>
                <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4"
                    placeholder="Enter A City/Region Here">

            </nav>
            <div ref="hero" class="flex flex-col items-center text-white bg-hero-background bg-center bg-cover py-40">
                <span class="m-0 text-2xl">Logo</span>
                <h1 class="text-5xl my-4">Find it. Tour it. Make it yours.</h1>
                <label for="search" class="hidden">Search</label>
                <input type="search" id="search" class="h-10 w-2/5 bg-[#374151] pl-4"
                    placeholder="Enter A City/Region Here">
            </div>
        </header>

        <main>
            <section class="py-4">
                <h2 class="text-2xl text-center py-3">Explore rentals in Accra</h2>
                <Carousel :value="apartments" :numVisible=5 :numScroll="3" :circular="true"
                    :responsiveOptions="responsiveOptions">
                    <template #item="{ data: apartment }">
                        <div class="mx-5">
                            <img :src="apartment.image[0].image" alt="Apartment" class="w-full">
                            <div class="pt-2">
                                <span class="text-xl">{{ apartment.name }}</span>
                                <!-- <p class="text-xl">{{ data. }}</p> -->
                                <p class="">{{ apartment.location.city }}</p>
                                <p class="">{{ apartment.price }}</p>
                            </div>
                        </div>
                    </template>
                </Carousel>
            </section>

            <section class="py-4">
                <h2 class="text-2xl text-center py-3">Browse apartments by type</h2>
                <Carousel :value="apartmentTypes" :numVisible=5 :numScroll="3" :circular="true" :autoplayInterval="3000"
                    :responsiveOptions="responsiveOptions">
                    <template #item="{ data: type }">
                        <div class="mx-5">
                            <img :src="type.image" alt="apartment type" class="w-full">
                            <div class="pt-2">
                                <span class="text-xl">{{ type.name }}</span>
                            </div>
                        </div>
                    </template>
                </Carousel>
            </section>
        </main>
    </div>
</template>
