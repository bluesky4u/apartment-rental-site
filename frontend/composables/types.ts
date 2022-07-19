export interface Apartment {
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

export interface ApartmentLocation {
    id: number;
    city: string;
    long: number;
    lat: number;
}

export interface ApartmentType {
    id: number;
    name: string;
    image: string;
}

export interface ApartmentImage {
    id: number;
    image: string;
}
