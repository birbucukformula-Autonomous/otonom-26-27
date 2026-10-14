# Git Push Restriction Rule

> KESİN KURAL: Kullanıcıdan açık ve yazılı izin almadan ASLA `git push` komutu çalıştırılamaz.

## Prensipler
1. `git push` komutu, uzaktaki repoyu doğrudan değiştirdiği için kullanıcı açıkça "push yap", "değişiklikleri pushla" veya "git push çalıştır" demediği sürece YASAKTIR.
2. Yerel Git işlemleri (`git status`, `git add`, `git commit`, `git checkout`, `git branch`, `git diff`) yerel repoda güvenle yapılabilir.
3. Çalışma bittiğinde yapılan yerel commit'ler kullanıcıya bildirilir ve push onayı sorulur.
