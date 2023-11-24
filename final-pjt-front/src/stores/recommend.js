import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useAddressStore } from '@/stores/address'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
 
export const useRecommendStore = defineStore('recommend', () => {
  const rankedProductsList = ref([])
  const userStore = useUserStore()
  const financeStore = useFinanceStore()

  // 상품 순위 필터링 후 반환
  const rankingProduct = (payload) => {
    console.log(payload);
    axios({
        method: 'post',
        url: `http://127.0.0.1:8000/finances/filter-user/`,
        data: payload,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
    }).then((res) => {
      const tempProducts = ref([])
      tempProducts.value = res.data.map(entry => entry[0])
      const filteredProductCodes = tempProducts.value.map(productCode => productCode)
      console.log('상품 추천이 완료되었습니다.')
      return filteredProductCodes
    }).then((filteredProductCodes) => {
      rankedProductsList.value = filteredProductCodes.map(productCode => {
        return financeStore.allProductList.find(product => product.product.fin_prdt_cd === productCode) || null
      })
      console.log(rankedProductsList.value);
    }).catch(err => console.log(err))
  }
  // 추천 업데이트
  const updateRecommendation = (selectedOptions) => {
    const payload = {}
  
    if (selectedOptions.age) {
      payload.age = userStore.user.age
    }
    if (selectedOptions.gender) {
      payload.gender = userStore.user.gender
    }
    if (selectedOptions.mbti) {
      payload.mbti = userStore.user.mbti
    }
    if (selectedOptions.salary) {
      payload.salary = userStore.user.salary
    }  
    // 추천 상품 요청
    console.log(payload);
    financeStore.getAllProducts()
    rankingProduct(payload)
  }

  const calculateAssetGrowthRate = (finPrdtCd, saveTerm) => {
    // 1. finPrdtCd에 해당하는 상품 찾기
    financeStore.getAllProducts()

    const targetProduct = financeStore.allProductList.find(product => product.product.fin_prdt_cd === finPrdtCd)

    // 2. 예금인지 적금인지 체크
    const intr_rate_type_nm = ref('')
    if (targetProduct.product.fin_prdt_nm.includes('예금')) {
      // 2-1. 예금이면
      intr_rate_type_nm.value = '단리'
    } else {
      intr_rate_type_nm.value = '복리'
    }
    
    // 3. 선택한 예치 기간에 해당하는 옵션 찾기
    const options = targetProduct.options    
    const selectedOption = options.find(option => option.save_trm === saveTerm)

    // 만약 옵션이 없으면
    if (!selectedOption) {
      console.error(`No option found for the selected deposit period: ${saveTerm}`)
      return null
    }
    // 저축 금리, 우대금리
    const interestRate = selectedOption.intr_rate
    const interestRate2 = selectedOption.intr_rate2

    return {intr_rate_type_nm, interestRate, interestRate2}
  }

// 원금(principal), 연이율(interestRate), 개월 수(months)를 받아 단리를 계산하는 함수
const calculateSimpleInterest = (principal, interestRate, months) => {
  const monthlyInterestRate = interestRate / 12 / 100; // 연이율을 월 이율로 변환
  const interest = principal * monthlyInterestRate * months;
  const totalAmount = principal + interest;
  return { interest, totalAmount };
};

// 원금(principal), 연이율(interestRate), 개월 수(months)를 받아 복리를 계산하는 함수
const calculateCompoundInterest = (principal, interestRate, months) => {
  const monthlyInterestRate = interestRate / 12 / 100; // 연이율을 월 이율로 변환
  const totalAmount = principal * Math.pow(1 + monthlyInterestRate, months);
  const interest = totalAmount - principal;
  return { interest, totalAmount };
};


// 유저 정보 갱신 여부 확인

// 유저 정보 갱신 된 날짜가 오늘이 아니면 날짜 차이만큼 부리 하기

// 부리 할 때는 유저가 가입한 상품들에 담긴 정보(예 : ['231101', 'WB00010', 200] 각각 상품 가입 날짜, 금융상품코드, 월 납입금)를 이용한다. 금융상품코드는 상품을 조회하여 금리와 예치기간과 금리 타입을 가져올 때 사용하고, 가입날짜와 월납입금은 현재 그 상품에 들어간 원금과 발생할 이자를 계산하는데 사용한다.  

const updateAsset = async () => {
  const userProducts = userStore.user.financial_products || [];
  const currentDate = new Date();

  let totalAmount = 0;
  let productDetail;
  let joinDate;
  let productCode;
  let monthlyPayment;

  for (const productInfo of userProducts) {
    joinDate = new Date(
      2000 + parseInt(productInfo[0].substring(0, 2)),
      parseInt(productInfo[0].substring(2, 4)) - 1,
      parseInt(productInfo[0].substring(4, 6))
    );

    productCode = productInfo[1];
    monthlyPayment = productInfo[2];

    for (const term of [6, 12, 24, 36]) {
      productDetail = calculateAssetGrowthRate(productCode, term);
      if (productDetail) {
        break;
      }
    }

    const { intr_rate_type_nm, interestRate, interestRate2 } = productDetail;

    if (intr_rate_type_nm === '단리') {
      const updatedPrincipal = calculateUpdatedPrincipal(monthlyPayment, interestRate, joinDate);
      totalAmount = totalAmount === null ? calculateDailyInterest(updatedPrincipal, interestRate) : totalAmount + calculateDailyInterest(updatedPrincipal, interestRate);
    } else {
      const updatedPrincipal = calculateUpdatedPrincipal(monthlyPayment, interestRate, joinDate);
      totalAmount = totalAmount === null ? calculateCompoundInterestDaily(updatedPrincipal, interestRate) : totalAmount + calculateCompoundInterestDaily(updatedPrincipal, interestRate);
    }
  }
  if (!isNaN(totalAmount) && totalAmount !== 0) { // totalAmount가 계산되지 않은 경우 갱신을 하지 않음

    console.log('totalAmount', totalAmount);
    console.log(totalAmount);
    userStore.userUpdate({
      username: userStore.user.username,
      email: userStore.user.email,
      nickname: userStore.user.nickname,
      age: userStore.user.age,
      address: userStore.user.address,
      salary: userStore.user.salary,
      money: userStore.user.money + totalAmount,
      target_asset: userStore.user.target_asset,
      mbti: userStore.user.mbti.toUpperCase(),
    });
  }
};

const calculateUpdatedPrincipal = (monthlyPayment, interestRate, joinDate) => {
  const currentDate = new Date();
  const daysDiff = Math.floor((currentDate - joinDate) / (1000 * 60 * 60 * 24));
  const dailyInterestRate = interestRate / 12 / 100 / 30;
  const totalAmount = monthlyPayment * ((Math.pow(1 + dailyInterestRate, daysDiff)) - 1) / dailyInterestRate;
  return totalAmount;
};

const calculateDailyInterest = (principal, annualInterestRate) => {
  const dailyInterestRate = annualInterestRate / 36500;
  const interest = principal * dailyInterestRate;
  return interest;
};

const calculateCompoundInterestDaily = (principal, annualInterestRate, period) => {
  const dailyInterestRate = annualInterestRate / 36500;
  const totalAmount = principal * Math.pow((1 + dailyInterestRate), period);
  const interest = totalAmount - principal;
  return interest;
};

  return { rankedProductsList, rankingProduct, updateRecommendation, calculateAssetGrowthRate, updateAsset }
}, { persist: true })
