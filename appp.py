import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="حاسبة وزن الأعمال الرقابية الميدانية", page_icon="🏛️", layout="centered")

st.image("REGA_LOGO_.png", width=200)

# العنوان الرئيسي
st.title("حاسبة وزن الأعمال الرقابية الميدانية")

# جدول الأوزان الثابتة
fixed_weights = {
    "المزادات": 2,
    "بيع على الخارطة (وافي) - رصد وتسليم المحاضر": 5,
    "لوحة ميدانية تصحيحية - بيانات المعلن غير متوفرة": 45,
    "لوحة ميدانية تصحيحية - بيانات المعلن متوفرة": 30,
    "لوحة ميدانية": 60,
    "الزيارات الميدانية - مفتوحة": 17,
    "الزيارات الميدانية - الحالات الأخرى (مغلق - غير موجود - خارج الاختصاص)": 25

}

# اختيار نوع النشاط
activity = st.selectbox("اختر نوع النشاط:", list(fixed_weights.keys()))

# إدخال عدد العمليات المنفذة
executed = st.number_input("أدخل عدد العمليات المنفذة:", min_value=0, value=0, step=1)

# عند الضغط على الحساب
if st.button("احسب المتبقي"):
    target = fixed_weights[activity]
    remaining = target - executed

    st.markdown("---")
    st.subheader("النتائج:")

    st.write(f"**النشاط المختار:** {activity}")
    st.write(f"**الوزن المستهدف:** {target}")
    st.write(f"**عدد العمليات المنفذة:** {executed}")

    if remaining >= 0:
        st.success(f"المتبقي لتحقيق المستهدف: {remaining}")
    else:
        st.warning(f"تم تجاوز المستهدف بمقدار: {abs(remaining)} ✅")

    st.markdown("---")
