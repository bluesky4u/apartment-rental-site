import type { RouterOptions } from '@nuxt/schema'

// https://router.vuejs.org/api/interfaces/routeroptions.html
export default <RouterOptions> {
    scrollBehavior: (to, from, savedPosition) => {
        console.log(savedPosition)
        if (savedPosition) {
            return {top: savedPosition.top, behavior: 'smooth'}
        } else {
            return {top: 0, behavior: 'smooth'}
        }
    },
}