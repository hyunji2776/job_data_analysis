import streamlit as st
import pandas as pd
from PIL import Image
import plotly
import os

st.set_page_config(
     page_title="Job Data Analysis App",
     page_icon="📊",
     layout="wide",
     initial_sidebar_state="expanded",
 )



current_file = os.path.abspath(os.path.dirname(__file__))

data = pd.read_csv(current_file+"/../data/jobkorea_data.csv")


st.title('📊 잡코리아 채용 정보를 통한 구직 트렌드 분석 📊')
st.subheader('0515-0517 mini project')
st.text('👩‍💻김현지, 👩‍💻이우윤, 👩‍💻김혜진')


with st.container():
    st.divider()
    st.header('주제 선정 이유')
    image = Image.open(current_file+'/job1.png')

    st.image(image, width=600)
    st.markdown('''1. 모두가 구직자의 입장에서 구직 플랫폼인 '잡코리아' 데이터 분석을 통해 구직의 트렌드 분석 및 예측
2. 조원들이 관심 있는 주제를 선정하여 분석 과정에 흥미 유발''')
    # 구직자의 입장 : bold

with st.container():
    st.divider()
    st.header('작업과정')

    st.subheader('1. 데이터 선정')
    st.subheader('데이터 정보: 잡코리아 채용 정보 💼')
    st.dataframe(data, use_container_width=True)

    st.subheader('2. 데이터로 알고 싶은 내용 정의')
    st.markdown('''1. 연도별 채용 공고 키워드 분석
2. 업종별 급여 차이 분석
3. 연도별 X 학력별 수요  → 채용에 따른 경력과 학력 비교''')

    st.subheader('3. 데이터 전처리')
    st.markdown('''- 2020년, 2021년에 비해 상대적으로 적은 데이터인 2019년 데이터 제외
    - :green[2019, 2020, 2021 년도 데이터인데 2020년도는  39027 개, 2021년도는 15781개 인거에 비해 2019년도는 90개라서 빼기로 했다.  (2019년도 빼기)]
    
- 데이터에서 Null 값이 많은 ‘`업종직종정보명`**'**  분석에서 제외
    
    
- 시급, 월급, 연봉이 구분되어 있지 않은 것으로 판단한 ‘`급여수준정보명`' 칼럼 금액 분류
    1. 데이터 전처리
        1. NaN → 0 으로 처리
        2. “i만원 ~ j만원”같은 급여금액은 i와 j의 평균값으로 대치
    2. 급여별로 연봉/월급/단기 나눔. 각각에 적절하게 단위 지정해 비교하기로 했습니다. 
        
        연봉 - 1000만원 이상
        
        월급 - 100만원 이상
        
        단기 - 0원 이상
        

- `경력조건정보명`  칼럼의 ‘신입/경력’ 항목들을 ‘경력’으로 대치.
    - ‘신입’, ‘경력’, ‘신입/경력’, ‘관계없음’ 의 항목을 갖는 `경력조건정보명`  칼럼의 ‘신입/경력’이 ‘신입’과 ‘경력’ 모두에 속하는지, 아예 관계 없는 지 의문을 가짐
    - 따라서 **‘`경력년수정보명`**' 칼럼과 함께 확인한 뒤, ‘1년 미만’의 구직 정보가 없다는 것을 확인해 해당 데이터는 ‘신입’이 아닌 ‘경력’ 을 의미한다고 판단.
    - 모두 ‘경력’으로 처리''')

    st.subheader('4. 데이터 시각화')
    st.markdown('''- 업종마다 급여 차이를 표현하기 위해 scatter 그래프로 최저와 최고점 나타냄
- 업종에서 연봉기준으로 높고 낮음을 bar 그래프로 차이를 비교
- 연도별로 가장 인기 많았던 키워드를 Wordcloud 표현
- 경력과 학력을 2020년도와 2021년도 pie그래프로 비교''')

    st.subheader('5. 인사이트 도출 및 결론')
    st.markdown('''- 해당 분석 결과로 **구직자 입장에서는** 연도별로 구인을 많이 한 업종, 업종 별 급여 차이, 2020년과 2021년의 구인업체에서 요구하는 경력,학력의 변화를 확인할 수 있었다.
    
    
- 그러나 동일 공고 데이터에서 채용공고 키워드가 너무 중구난방으로 적혀 있었다. 이에 따라 많은 구직자들이 이용하는 플랫폼인 ‘잡코리아’에서 공고를 선별하기 어려울 것이라고 생각되었다.
- 또한 급여데이터에서 ‘실제 이 금액을 준다고..?’라고 생각될 만큼 정보의 신뢰성이 의심되는 데이터가 있었다.
- 따라서 **잡코리아에서** 채용공고 정보 검증 이후에 공고를 업로드한다면 구직자들에게 정확한 정보를 제공할 수 있을 것으로 생각된다.''')

with st.container():
    st.divider()
    st.header('애먹었던 점, 개선방안(에러를 만나고 -> 처리하는 과정 Trouble shooting)')

    st.subheader('1. ')
    st.error('해당채용공고키워드명에서 키워드를 전처리 하는 과정에서 너무 많은 키워드가 있어서 분류 기준 선정이 어려웠음 ', icon="🚨")
    st.info(' 몇 번의 키워드 추출을 통해 반복되는 키워드가 있음을 확인하고 상단에 나오는 3개의 키워드만을 분석에 사용하는 것으로 결정', icon="ℹ️")

    st.subheader('2. ')
    st.error('plotly그래프를 streamlit에서 동적으로 접근 가능하게 하고 싶었다.', icon="🚨")
    st.info('plotly를 html파일로 변환해서 streamlit에서 components.html로 html파일을 받아 그려내는데 성공함.', icon="ℹ️")
    
    st.subheader('3. ')
    st.error('streamlit 으로 그래프  이미지를 2개 넣고 표현하다보니, 이미지가 작고 생각한 모양이 아니였다.', icon="🚨")
    st.info('ploty에 관한 다양한 라이브러리로 그래프를 합치고, html로 만들어서 streamlit으로도 표현 할 수 있었다. ', icon="ℹ️")


with st.container():
    st.divider()
    st.header('소감') 
    col_hyunji, col_wooyoon, col_hyejin = st.tabs(["김현지", "이우윤", "김혜진"])

    with col_hyunji:
        st.subheader('김현지')
        st.markdown('''Streamlit을 배우고 바로 프로젝트를 시작하게 되어 처음엔 어떻게 구현해야 할지 막막했지만, 
'집단지성'의 힘으로 조원들과 아이디어 회의를 통해 데이터 분석 및 웹페이지 구현까지 마칠 수 있었습니다.

혼자만의 에러가 아닌 조원들의 에러도 함께 보면서 에러를 처리하는 과정을 경험할 수 있어서 좋았습니다
이제는 코드를 치면서 에러를 마주해도 조금은 덜 슬프지 않을까,,생각됩니다!😭''')
    with col_wooyoon:
        st.subheader('이우윤')
        st.markdown('''1. pandas도 익숙해지지 않은 채로 갑작스레😮 마주하게 된 프로젝트였습니다.
2. 프로젝트 초반에 데이터를 확인하며 알고 싶었던 내용에 대해 전부 해결하고 마칠 수 있어 뿌듯✌합니다.
3. 좋은 팀원들을 만나 수월하게 프로젝트를 진행할 수 있어서 즐거😍웠습니다.
4. 개인적으로도 데이터 분석의 툴을 활용하는 실력이 향상된 것 같아 만족🤘합니다.''')

    with col_hyejin:
        st.subheader('김혜진')
        st.markdown('''수업때 배운 내용이지만 아직 익숙하지 않아서 걱정되었지만,

팀원들💕의 도움으로 한개씩 해결할 수 있었고,

될까? 하는 부분도 다 가능하게 되어서 신기했습니다.

주제를 정할 때 어려움 없이 뜻이 맞아서 주제 정하자마자 데이터를 분석하고
계획한 바를 다 이루게 된거 같아서 재밌었습니다.

이번 프로젝트로 정말 많은 것을 배우고 성장 할 수 있었던 시간이였습니다.😂''')