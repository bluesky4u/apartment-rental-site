import { Apartment } from "./types"

const fetchOptions = {
    baseURL: "http://localhost:8000/v1/"
}

export const fetchApartments = (params: any) => {
    return useFetch<Apartment[]>("apartments/", {...params, ...fetchOptions})
}