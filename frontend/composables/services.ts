import { Apartment, ApartmentType } from "./types"
const fetchOptions = {
    baseURL: 'http://sulleyrydt8.pythonanywhere.com/v1/',
}

export const fetchApartments = (params: any = {}) => useFetch<Apartment[]>("apartments/", { ...params, ...fetchOptions })

export const fetchApartmentTypes = (params: any = {}) => useFetch<ApartmentType[]>("apartment-type/", { ...params, ...fetchOptions })

export const fetchApartmentDetails = (id: string, params: any = {}) => useFetch<Apartment>(`apartments/${id}`, { ...params, ...fetchOptions })
