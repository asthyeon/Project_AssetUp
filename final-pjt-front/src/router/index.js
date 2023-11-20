import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
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
			path: '/articles',
			name: 'articles',
			component: ArticleView
		},
    {
			path: '/article-create',
			name: 'article_create',
			component: ArticleCreateView
		},
    {
			path: '/article-detail/:article_id',
			name: 'article_detail',
			component: ArticleDetailView
		},
		{
			path: '/article-update/:article_id',
			name: 'article_update',
			component: ArticleUpdateView
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
