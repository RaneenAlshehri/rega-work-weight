import streamlit as st
import json

# إعدادات الصفحة
st.set_page_config(page_title="حاسبة وزن الأعمال الرقابية الميدانية", page_icon="🏛️", layout="centered")

# عرض الشعار
st.image("REGA_LOGO_.png", width=200)

# العنوان الرئيسي
st.title("حاسبة وزن الأعمال الرقابية الميدانية")

# قراءة الأوزان من ملف خارجي
with open("weights.json", "r", encoding="utf-8") as f:
    fixed_weights = json.load(f)

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
