import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  // 금융회사 목록
  const companys = ref([])
  // 정기예금 상품 목록
  const depositProductList = ref([])
  // 정기예금 옵션 목록
  const depositProductOptionList = ref([])
  // 적금 상품 목록
  const savingProductList = ref([])
  // 적금 옵션 목록
  const savingOptionList = ref([])

  const getCompanys = function () {
    axios({
        method: 'get',
        url: `${API_URL}/finances/get-companys/`
    }).then(res => {
        console.log('금융회사 조회 완료')
        companys.value = res.data
    }).catch(err => console.log(err))
  }

  const filteredProducts = ref([])

  // 상품 검색
  const searchProducts = function (fin_co_no, save_trm) {
      fin_co_no = fin_co_no || '전체'
      save_trm = save_trm || 0
      console.log(fin_co_no, save_trm)
    axios({
        method: 'get',
        url: `${API_URL}/finances/search-deposit-products/${fin_co_no}/${save_trm}/`
    }).then(res => {
        console.log('검색 완료')
        filteredProducts.value = res.data
        console.log(filteredProducts.value)
        console.log(filteredProducts.value.length)
    }).catch(err => console.log(err))
  }

  // 예금 상품 목록 조회
  const getDepositProducts = function () {
    axios({
        method: 'get',
        url: `${API_URL}/finances/get-deposit-products/`
    }).then(res => {
        console.log('예금 상품 조회 완료')
        depositProductList.value = res.data
    }).catch(err => console.log(err))
  }
  
  // 적금 상품 목록 조회
  const getSavingProducts = function () {
    axios({
        method: 'get',
        url: `${API_URL}/finances/get_saving_products/`
    }).then(res => {
        console.log('적금 상품 조회 완료')
        savingProductList.value = res.data
    }).catch(err => console.log(err))
  }

  // 단일 예금 상품
  const depositProduct = ref(null)

  // 단일 예금 상품 상세 정보 조회
  const getDepositProductDetail = function (finPrdtCd) {
    axios({
        method: 'get',
        url: `${API_URL}/finances/get-deposit-product-detail/${finPrdtCd}/`
    }).then(res => {
        console.log('단일 예금 상품 상세 조회 성공')
        console.log(res.data)
        depositProduct.value = res.data

    }).catch(err => console.log(err))
  }

  // 단일 예금 상품의 옵션 목록 조회
  const getDepositProductOptions = function (finPrdtCd) {
    axios({
        method:'get',
        url: `${API_URL}/finances/get-deposit-product-options/${finPrdtCd}/`
    }).then(res => {
        console.log('단일 예금 상품 옵션 조회 성공');
        depositProductOptionList.value = res.data
        console.log(depositProductOptionList.value)
    }).catch(err => console.log(err))
  }

  const depostiOptionLIst = ref([])

  // 예금 옵션 조회
  const getDepositOptions = function () {
    axios({
        method:'get',
        url: `${API_URL}/finances/get-deposit-options/`
    }).then(res => {
        console.log('예금 상품 옵션 조회 성공')
        depostiOptionLIst.value = res.data

    }).catch(err => console.log(err))
  }

  const getInterestRate = function (options, term) {
    const option = options.find(opt => opt.save_trm === term)
    return option ? option.intr_rate : '--'
  }

  const columnSortStates = {
    dcls_month: false,
    kor_co_nm: false,
    fin_prdt_nm: false,
    6: false,
    12: false,
    24: false,
    36: false
  }

  // 상품 정렬
  const sortProducts = function (key) {
    console.log('정렬되었습니다.')
    const isSorted = columnSortStates[key]

    Object.keys(columnSortStates).forEach(column => {
        if (column !== key) {
            columnSortStates[column] = false
        }
    })

    if (key === 'dcls_month' || key === 'fin_prdt_nm' || key === 'kor_co_nm') {
        filteredProducts.value.sort((a, b) => {
            const valueA = a.deposit_product[key]
            const valueB = b.deposit_product[key]

            return isSorted ? valueB.localeCompare(valueA) : valueA.localeCompare(valueB);
        });
    } else if ([6, 12, 24, 36].includes(key)) {
        const term = Number(key)
        console.log(term)
        filteredProducts.value.sort((a, b) => {
            const optionA = a.options.find(opt => opt.save_trm === term)
            const optionB = b.options.find(opt => opt.save_trm === term)

            if (!optionA) return 1
            if (!optionB) return -1

            if (optionA && optionB) {  
                return isSorted ? optionA.intr_rate - optionB.intr_rate : optionB.intr_rate - optionA.intr_rate
            } else {
                return 0
            }
        })
    }
    columnSortStates[key] = !isSorted
  }

  return {
    companys,
    depositProductList, depositProduct, depostiOptionLIst, depositProductOptionList,
    savingProductList, savingOptionList,
    getCompanys, getDepositProducts, getDepositOptions, getDepositProductOptions, getDepositProductDetail,
    getSavingProducts,
    filteredProducts, searchProducts, sortProducts }
}, { persist: true })
