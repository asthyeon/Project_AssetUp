import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import BoardArticleView from '@/views/BoardArticleView.vue'
import BoardArticleCreateView from '@/views/BoardArticleCreateView.vue'
import BoardArticleDetailView from '@/views/BoardArticleDetailView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import FinanceComparsionView from '@/views/FinanceComparsionView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/compare',
      name: 'compare',
      component: FinanceComparsionView
    },
    {
      path: '/product-detail/:fin_prdt_cd',
      name: 'product_detail',
      component: ProductDetailView
    },
    {
		path: '/signup',
		name: 'signup',
		component: SignUpView
	},
    {
		path: '/login',
		name: 'login',
		component: LogInView
	},
    {
		path: '/board',
		name: 'board',
		component: BoardArticleView
	},
    {
		path: '/board-create',
		name: 'board_create',
		component: BoardArticleCreateView
	},
    {
		path: '/board-detail/:id',
		name: 'board_detail',
		component: BoardArticleDetailView
	},
    {
		path: '/map',
		name: 'map',
		component: MapView
	},
    {
		path: '/exchange',
		name: 'exchange',
		component: ExchangeView
	},
  ]
})

// 메인페이지 로그인 상태로만 이용 가능
router.beforeEach((to, from) => {
  const userStore = useUserStore()
  if (to.name === 'main' && !userStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login'}
  }
  if ((to.name === 'signup' || to.name === 'login') && (userStore.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'main' }
  }
})
export default router
