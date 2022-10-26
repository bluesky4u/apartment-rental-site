import { Apartment, ApartmentType } from "./types"
const fetchOptions = {
    baseURL: 'https://sulleyrydt8.pythonanywhere.com/v1/',
}

// const fetchOptions = {
//     baseURL: 'http://localhost:8000/v1/',
// }


export const fetchApartments = (params: any = {}) => useFetch<Apartment[]>("apartments/", { ...params, ...fetchOptions })

export const fetchApartmentTypes = (params: any = {}) => useFetch<ApartmentType[]>("apartment-type/", { ...params, ...fetchOptions })

export const fetchApartmentDetails = (id: string, params: any = {}) => useFetch<Apartment>(`apartments/${id}`, { ...params, ...fetchOptions })

export const searchApartments = (query: any = {}) => fetchApartments({ params: { ...query }, key: `apartments/?search=${query.min_price}-${query.max_price}-${query.rooms}-${query.location__city}-${query.search}-` })