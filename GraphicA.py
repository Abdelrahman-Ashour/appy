import streamlit as st
import webbrowser

def open_whatsapp(number):
    url = f"https://wa.me/{number}"
    webbrowser.open(url)

def open_email(email):
    url = f"mailto:{email}"
    webbrowser.open(url)

def open_facebook(username):
    url = f"https://www.facebook.com/{username}"
    webbrowser.open(url)

# تحديد الصفحات
st.sidebar.title("التنقل")
page = st.sidebar.radio("انتقل إلى:", ["الصفحة الرئيسية", "طلب الخدمات", "اتصل بنا"])

if page == "الصفحة الرئيسية":
    st.title("مرحبًا بكم في موقعنا")
    st.write("هذه هي الصفحة الرئيسية حيث يمكنكم معرفة المزيد عن خدماتنا.")

elif page == "طلب الخدمات":
    st.title("طلب الخدمات")
    st.write("يرجى ملء النموذج التالي لطلب الخدمة.")
    name = st.text_input("الاسم:")
    service_type = st.selectbox("نوع الخدمة:", ["تصميم جرافيك", "برمجة مواقع", "إصلاح أجهزة إلكترونية"])
    details = st.text_area("التفاصيل:")
    if st.button("إرسال الطلب"):
        st.success("تم إرسال طلبك بنجاح! سنتواصل معك قريبًا.")

elif page == "اتصل بنا":
    st.title("اتصل بنا")
    if st.button("💬 whatsapp"): 
        open_whatsapp("201553012416")
    if st.button("📧 gmail"): 
        open_email("alordashour@gmail.com")
    if st.button("open our facebook"): 
        open_facebook("abdallah13a")
