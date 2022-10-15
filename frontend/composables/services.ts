import { Apartment } from "./types"


export const fetchApartments = (params: any) => {
    return useFetch<Apartment[]>("http://localhost:8000/v1/apartments/", params)
}