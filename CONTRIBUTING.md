# 🤝 Katkı Sağlama & Teslim (Submission) Rehberi

Bu rehber, eğitim görevlerinizi tamamlarken ve repoya teslim yaparken izlemeniz gereken Git iş akışını (workflow) açıklar. Takım içi profesyonel yazılım kültürünün en önemli parçası Git disiplinidir.

---

## 📌 Temel Kurallar

1. **`main` Dalına Doğrudan Commit / Push Kesinlikle Yasaktır:** Tüm teslimler bir dal (branch) üzerinden Pull Request (PR) açılarak yapılır.
2. **Kişisel Klasör Kuralı:** Çalışmalarınızı **yalnızca** `tasks/<task-adi>/submissions/<ad_soyad>/` dizinine ekleyin. Bu dizin dışındaki dosyalarda değişiklik yapmayın.
3. **Temiz Commit Geçmişi:** Anlamsız commit mesajları (`asdasd`, `update`, `fix`) yerine açıklayıcı mesajlar kullanın.

---

## 🛠️ Adım Adım Teslimat Akışı

### 1. Güncel Kodu Çekin
Çalışmaya başlamadan önce her zaman `main` dalının en güncel halini alın:
```bash
git checkout main
git pull origin main
```

### 2. Yeni Bir Görev Dalı (Branch) Açın
Dal isminiz görevi ve adınızı içermelidir:
`submission/<ad-soyad>/<task-kodu>`

Örnekler:
```bash
git checkout -b submission/ahmet-yilmaz/task-01
git checkout -b submission/ayse-demir/task-02
```

### 3. Görevinizi Tamamlayın ve Dosyalarınızı Ekleyin
İlgili görevin altındaki `submissions/` dizinine kendi ad ve soyadınızla bir klasör oluşturun:
```text
tasks/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
├── sunum.pdf
└── ozet_rapor.md
```

### 4. Yalnızca Kendi Klasörünüzü Git'e Ekleyin
```bash
git status
git add tasks/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
```

### 5. Anlamlı Bir Commit Mesajı Yazın
Format: `feat(<task>): <ad soyad> <yaptığınız işlem>`
```bash
git commit -m "feat(task-01): Ahmet Yilmaz otonom mimari sunum teslimi"
```

### 6. Dalınızı Uzak Sunucuya Gönderin
```bash
git push origin submission/ahmet-yilmaz/task-01
```

### 7. GitHub Üzerinden Pull Request (PR) Açın
1. GitHub reponuza gidin. Açtığınız dal için **"Compare & pull request"** butonunu göreceksiniz.
2. Karşılaştırma hedefinin `base: main` olduğundan emin olun.
3. Başlık olarak commit mesajınızı kullanın.
4. Açıklama kısmında çıkan kontrol listesindeki kutucukları işaretleyin (`[x]` şeklinde).
5. Mentörünüzü "Reviewer" olarak atayın.

---

## 🔍 Code Review ve Geri Bildirim Süreci

* PR açıldıktan sonra takım lideri veya mentörler kodunuzu / sunumunuzu inceler.
* İstenen bir düzeltme olursa aynı dal üzerinde çalışmaya devam edip tekrar commit + push yapabilirsiniz; PR otomatik güncellenir.
* Tüm kriterler sağlandığında PR'ınız onaylanır ve `main` dalına merge edilir. Tebrikler, görevi tamamladınız!
