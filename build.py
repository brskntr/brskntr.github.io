"""
Builds the site: the developer page, and the privacy policy of Whose Bag? in six languages.

    python3 build.py

The policy text lives below, one block per language; edit it here and rebuild, never the HTML.
"""

import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "Barış Kantar"
EMAIL = "bariskantar@gmail.com"
UPDATED = {"en": "8 November 2026", "tr": "8 Kasım 2026", "es": "8 de noviembre de 2026",
           "pt": "8 de novembro de 2026", "de": "8. November 2026", "fr": "8 novembre 2026"}
GOOGLE_PARTNERS = "https://policies.google.com/technologies/partner-sites"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
UNITY_PRIVACY = "https://unity.com/legal/privacy-policy"
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"

# Order of the language switcher; English sits at the folder root.
LANGS = [("en", "English"), ("tr", "Türkçe"), ("es", "Español"), ("pt", "Português (BR)"), ("de", "Deutsch"), ("fr", "Français")]
HTML_LANG = {"en": "en", "tr": "tr", "es": "es", "pt": "pt-BR", "de": "de", "fr": "fr"}

# Each policy: a title, the "last updated" label, and sections of (heading, [paragraphs]).
# Paragraphs may hold {email}, {google_partners}, {google_privacy}, {unity_privacy}, {apple_privacy} links.
P = {
    "en": {
        "title": "Privacy Policy",
        "updated": "Last updated",
        "intro": "This policy explains what information the game Whose Bag? (“the game”) uses, why, and the choices you have. The game is made by {developer}, an independent developer (“I”, “me”).",
        "sections": [
            ("What the game keeps on your device", [
                "Your progress, coins, settings (sound, language) and whether you have bought “Remove ads” are saved only on your device. They are not sent to me. The game has no accounts and never asks for your name, email address or other contact details.",
            ]),
            ("Advertising (Google AdMob)", [
                "The game shows ads through Google AdMob, a service of Google. To show and measure ads and to prevent fraud, Google may collect: your device’s advertising identifier (on iOS, only if you allow tracking), your IP address, device and app information such as model, operating system and language, an approximate location derived from your IP address, and how you interact with ads.",
                "Where the law requires it (the European Economic Area, the United Kingdom and Switzerland), personalised ads are only shown with your consent. Without it, Google shows non-personalised ads. How Google uses this information is explained at {google_partners} and in {google_privacy_link}.",
            ]),
            ("Your choices", [
                "If you are in the EEA, the UK or Switzerland, the game asks for your consent the first time it starts. You can change your answer at any time in the game: Settings → Ad privacy choices.",
                "On iPhone and iPad, iOS asks whether the game may track you. You can change this at any time in the device’s Settings → Privacy & Security → Tracking. You can also reset your advertising identifier in your device settings.",
                "Buying “Remove ads” stops the ads shown between levels. Rewarded ads, which you choose to watch for a hint or extra time, stay available.",
            ]),
            ("In-app purchases", [
                "Purchases are made through the App Store and processed by Apple. I never receive your payment details. The game uses Unity In-App Purchasing by Unity Technologies to talk to the App Store; it checks your purchases on your device. See {apple_privacy_link} and {unity_privacy_link}.",
            ]),
            ("Children", [
                "The game is not directed at children under 13, and I do not knowingly collect personal information from them.",
            ]),
            ("Keeping and deleting data", [
                "Deleting the game deletes everything it saved on your device. Information collected by Google is kept and deleted under Google’s own policy.",
            ]),
            ("Changes", [
                "If this policy changes, the new version will be posted on this page with a new date.",
            ]),
            ("Contact", [
                "Questions about privacy: {email}",
            ]),
        ],
        "google_privacy": "Google’s Privacy Policy",
        "apple_privacy": "Apple’s Privacy Policy",
        "unity_privacy": "Unity’s Privacy Policy",
    },
    "tr": {
        "title": "Gizlilik Politikası",
        "updated": "Son güncelleme",
        "intro": "Bu politika, Whose Bag? (Kayıp Bagaj) oyununun (“oyun”) hangi bilgileri neden kullandığını ve senin hangi seçeneklerin olduğunu açıklar. Oyunu bağımsız geliştirici {developer} (“ben”) yapıyor.",
        "sections": [
            ("Oyunun cihazında sakladıkları", [
                "İlerlemen, jetonların, ayarların (ses, dil) ve “Reklamları kaldır”ı alıp almadığın yalnızca cihazında saklanır, bana gönderilmez. Oyunda hesap yoktur; adını, e-posta adresini ya da başka bir iletişim bilgini hiçbir zaman istemez.",
            ]),
            ("Reklamlar (Google AdMob)", [
                "Oyun reklamları Google’ın hizmeti olan Google AdMob üzerinden gösterir. Reklamları göstermek, ölçmek ve sahtekârlığı önlemek için Google şunları toplayabilir: cihazının reklam kimliği (iOS’ta yalnızca izlemeye izin verirsen), IP adresin, model, işletim sistemi ve dil gibi cihaz ve uygulama bilgileri, IP adresinden çıkarılan yaklaşık konum ve reklamlarla etkileşimin.",
                "Yasanın gerektirdiği yerlerde (Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre) kişiselleştirilmiş reklamlar yalnızca onayınla gösterilir; onay vermezsen Google kişiselleştirilmemiş reklam gösterir. Google’ın bu bilgileri nasıl kullandığı {google_partners} adresinde ve {google_privacy_link} içinde anlatılıyor.",
            ]),
            ("Seçeneklerin", [
                "AEA’da, Birleşik Krallık’ta ya da İsviçre’deysen oyun ilk açılışta onayını sorar. Cevabını oyunda istediğin zaman değiştirebilirsin: Ayarlar → Reklam gizlilik seçenekleri.",
                "iPhone ve iPad’de iOS, oyunun seni izleyip izleyemeyeceğini sorar. Bunu istediğin zaman cihazın Ayarlar → Gizlilik ve Güvenlik → İzleme bölümünden değiştirebilirsin. Reklam kimliğini de cihaz ayarlarından sıfırlayabilirsin.",
                "“Reklamları kaldır”ı satın almak bölüm aralarındaki reklamları kapatır. İpucu ya da ek süre için kendi isteğinle izlediğin ödüllü reklamlar kullanılabilir kalır.",
            ]),
            ("Uygulama içi satın almalar", [
                "Satın almalar App Store üzerinden yapılır ve Apple tarafından işlenir; ödeme bilgilerin bana hiçbir zaman ulaşmaz. Oyun App Store ile konuşmak için Unity Technologies’in Unity In-App Purchasing kitaplığını kullanır; satın almalarını cihazında doğrular. Bkz. {apple_privacy_link} ve {unity_privacy_link}.",
            ]),
            ("Çocuklar", [
                "Oyun 13 yaşından küçük çocuklara yönelik değildir ve onlardan bilerek kişisel bilgi toplamam.",
            ]),
            ("Verilerin saklanması ve silinmesi", [
                "Oyunu silmek, cihazında sakladığı her şeyi siler. Google’ın topladığı bilgiler Google’ın kendi politikasına göre saklanır ve silinir.",
            ]),
            ("Değişiklikler", [
                "Bu politika değişirse yeni hâli bu sayfada yeni tarihle yayınlanır.",
            ]),
            ("İletişim", [
                "Gizlilikle ilgili soruların için: {email}",
            ]),
        ],
        "google_privacy": "Google Gizlilik Politikası",
        "apple_privacy": "Apple Gizlilik Politikası",
        "unity_privacy": "Unity Gizlilik Politikası",
    },
    "es": {
        "title": "Política de privacidad",
        "updated": "Última actualización",
        "intro": "Esta política explica qué información usa el juego Whose Bag? (“el juego”), para qué y qué opciones tienes. El juego lo hace {developer}, un desarrollador independiente (“yo”).",
        "sections": [
            ("Lo que el juego guarda en tu dispositivo", [
                "Tu progreso, tus monedas, tus ajustes (sonido, idioma) y si compraste “Quitar anuncios” se guardan solo en tu dispositivo y no se me envían. El juego no tiene cuentas y nunca te pide tu nombre, correo electrónico ni otros datos de contacto.",
            ]),
            ("Publicidad (Google AdMob)", [
                "El juego muestra anuncios a través de Google AdMob, un servicio de Google. Para mostrar y medir anuncios y prevenir fraudes, Google puede recopilar: el identificador de publicidad de tu dispositivo (en iOS, solo si permites el rastreo), tu dirección IP, información del dispositivo y de la app como modelo, sistema operativo e idioma, una ubicación aproximada obtenida de tu IP y cómo interactúas con los anuncios.",
                "Donde la ley lo exige (Espacio Económico Europeo, Reino Unido y Suiza), los anuncios personalizados solo se muestran con tu consentimiento; sin él, Google muestra anuncios no personalizados. Cómo usa Google esta información se explica en {google_partners} y en la {google_privacy_link}.",
            ]),
            ("Tus opciones", [
                "Si estás en el EEE, el Reino Unido o Suiza, el juego te pide tu consentimiento la primera vez que se abre. Puedes cambiar tu respuesta cuando quieras en el juego: Ajustes → Opciones de privacidad de anuncios.",
                "En iPhone y iPad, iOS te pregunta si el juego puede rastrearte. Puedes cambiarlo cuando quieras en Ajustes del dispositivo → Privacidad y seguridad → Rastreo. También puedes restablecer tu identificador de publicidad en los ajustes del dispositivo.",
                "Comprar “Quitar anuncios” elimina los anuncios entre niveles. Los anuncios con recompensa, que eliges ver para obtener una pista o tiempo extra, siguen disponibles.",
            ]),
            ("Compras dentro de la app", [
                "Las compras se hacen en el App Store y las procesa Apple; nunca recibo tus datos de pago. El juego usa Unity In-App Purchasing, de Unity Technologies, para comunicarse con el App Store; verifica tus compras en tu dispositivo. Consulta la {apple_privacy_link} y la {unity_privacy_link}.",
            ]),
            ("Menores", [
                "El juego no está dirigido a menores de 13 años y no recopilo a sabiendas información personal de ellos.",
            ]),
            ("Conservación y eliminación de datos", [
                "Al borrar el juego se borra todo lo que guardó en tu dispositivo. La información que recopila Google se conserva y elimina según la política de Google.",
            ]),
            ("Cambios", [
                "Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha.",
            ]),
            ("Contacto", [
                "Preguntas sobre privacidad: {email}",
            ]),
        ],
        "google_privacy": "Política de privacidad de Google",
        "apple_privacy": "Política de privacidad de Apple",
        "unity_privacy": "Política de privacidad de Unity",
    },
    "pt": {
        "title": "Política de Privacidade",
        "updated": "Última atualização",
        "intro": "Esta política explica quais informações o jogo Whose Bag? (“o jogo”) usa, para quê e quais escolhas você tem. O jogo é feito por {developer}, um desenvolvedor independente (“eu”).",
        "sections": [
            ("O que o jogo guarda no seu dispositivo", [
                "Seu progresso, suas moedas, suas configurações (som, idioma) e se você comprou “Remover anúncios” ficam salvos apenas no seu dispositivo e não são enviados para mim. O jogo não tem contas e nunca pede seu nome, e-mail ou outros dados de contato.",
            ]),
            ("Publicidade (Google AdMob)", [
                "O jogo mostra anúncios pelo Google AdMob, um serviço do Google. Para exibir e medir anúncios e evitar fraudes, o Google pode coletar: o identificador de publicidade do seu dispositivo (no iOS, só se você permitir o rastreamento), seu endereço IP, informações do dispositivo e do app como modelo, sistema operacional e idioma, uma localização aproximada obtida pelo IP e como você interage com os anúncios.",
                "Onde a lei exige (Espaço Econômico Europeu, Reino Unido e Suíça), anúncios personalizados só são exibidos com o seu consentimento; sem ele, o Google mostra anúncios não personalizados. Como o Google usa essas informações está explicado em {google_partners} e na {google_privacy_link}.",
            ]),
            ("Suas escolhas", [
                "Se você estiver no EEE, no Reino Unido ou na Suíça, o jogo pede seu consentimento na primeira vez em que é aberto. Você pode mudar sua resposta quando quiser no jogo: Configurações → Opções de privacidade de anúncios.",
                "No iPhone e no iPad, o iOS pergunta se o jogo pode rastrear você. Você pode mudar isso quando quiser em Ajustes do dispositivo → Privacidade e Segurança → Rastreamento. Também pode redefinir o identificador de publicidade nos ajustes do dispositivo.",
                "Comprar “Remover anúncios” acaba com os anúncios entre as fases. Os anúncios com recompensa, que você escolhe assistir para ganhar uma dica ou tempo extra, continuam disponíveis.",
            ]),
            ("Compras no app", [
                "As compras são feitas pela App Store e processadas pela Apple; eu nunca recebo seus dados de pagamento. O jogo usa o Unity In-App Purchasing, da Unity Technologies, para se comunicar com a App Store; ele verifica suas compras no seu dispositivo. Veja a {apple_privacy_link} e a {unity_privacy_link}.",
            ]),
            ("Crianças", [
                "O jogo não é direcionado a crianças menores de 13 anos, e eu não coleto intencionalmente informações pessoais delas.",
            ]),
            ("Guarda e exclusão de dados", [
                "Apagar o jogo apaga tudo o que ele salvou no seu dispositivo. As informações coletadas pelo Google são guardadas e excluídas conforme a política do próprio Google.",
            ]),
            ("Alterações", [
                "Se esta política mudar, a nova versão será publicada nesta página com uma nova data.",
            ]),
            ("Contato", [
                "Dúvidas sobre privacidade: {email}",
            ]),
        ],
        "google_privacy": "Política de Privacidade do Google",
        "apple_privacy": "Política de Privacidade da Apple",
        "unity_privacy": "Política de Privacidade da Unity",
    },
    "de": {
        "title": "Datenschutzerklärung",
        "updated": "Zuletzt aktualisiert",
        "intro": "Diese Erklärung beschreibt, welche Informationen das Spiel Whose Bag? („das Spiel“) verwendet, wozu und welche Wahlmöglichkeiten du hast. Das Spiel stammt von {developer}, einem unabhängigen Entwickler („ich“).",
        "sections": [
            ("Was das Spiel auf deinem Gerät speichert", [
                "Dein Fortschritt, deine Münzen, deine Einstellungen (Ton, Sprache) und ob du „Werbung entfernen“ gekauft hast, werden nur auf deinem Gerät gespeichert und nicht an mich gesendet. Das Spiel hat keine Konten und fragt nie nach deinem Namen, deiner E-Mail-Adresse oder anderen Kontaktdaten.",
            ]),
            ("Werbung (Google AdMob)", [
                "Das Spiel zeigt Werbung über Google AdMob, einen Dienst von Google. Um Werbung anzuzeigen, zu messen und Betrug zu verhindern, kann Google Folgendes erheben: die Werbe-ID deines Geräts (unter iOS nur, wenn du Tracking erlaubst), deine IP-Adresse, Geräte- und App-Informationen wie Modell, Betriebssystem und Sprache, einen aus der IP-Adresse abgeleiteten ungefähren Standort sowie deine Interaktionen mit Werbung.",
                "Wo das Gesetz es verlangt (Europäischer Wirtschaftsraum, Vereinigtes Königreich und Schweiz), wird personalisierte Werbung nur mit deiner Einwilligung gezeigt; ohne sie zeigt Google nicht personalisierte Werbung. Wie Google diese Informationen nutzt, steht unter {google_partners} und in der {google_privacy_link}.",
            ]),
            ("Deine Wahlmöglichkeiten", [
                "Wenn du dich im EWR, im Vereinigten Königreich oder in der Schweiz befindest, fragt das Spiel beim ersten Start nach deiner Einwilligung. Du kannst deine Antwort jederzeit im Spiel ändern: Einstellungen → Werbe-Datenschutzoptionen.",
                "Auf iPhone und iPad fragt iOS, ob das Spiel dich tracken darf. Das kannst du jederzeit in den Geräteeinstellungen unter Datenschutz & Sicherheit → Tracking ändern. Deine Werbe-ID kannst du ebenfalls in den Geräteeinstellungen zurücksetzen.",
                "Der Kauf von „Werbung entfernen“ beendet die Werbung zwischen den Levels. Belohnte Werbung, die du freiwillig für einen Tipp oder zusätzliche Zeit ansiehst, bleibt verfügbar.",
            ]),
            ("In-App-Käufe", [
                "Käufe laufen über den App Store und werden von Apple abgewickelt; deine Zahlungsdaten erhalte ich nie. Das Spiel nutzt Unity In-App Purchasing von Unity Technologies, um mit dem App Store zu kommunizieren; es prüft deine Käufe auf deinem Gerät. Siehe {apple_privacy_link} und {unity_privacy_link}.",
            ]),
            ("Kinder", [
                "Das Spiel richtet sich nicht an Kinder unter 13 Jahren, und ich erhebe nicht wissentlich personenbezogene Daten von ihnen.",
            ]),
            ("Speicherung und Löschung", [
                "Wenn du das Spiel löschst, wird alles gelöscht, was es auf deinem Gerät gespeichert hat. Von Google erhobene Informationen werden nach Googles eigener Richtlinie gespeichert und gelöscht.",
            ]),
            ("Änderungen", [
                "Wenn sich diese Erklärung ändert, wird die neue Fassung mit neuem Datum auf dieser Seite veröffentlicht.",
            ]),
            ("Kontakt", [
                "Fragen zum Datenschutz: {email}",
            ]),
        ],
        "google_privacy": "Datenschutzerklärung von Google",
        "apple_privacy": "Datenschutzrichtlinie von Apple",
        "unity_privacy": "Datenschutzrichtlinie von Unity",
    },
    "fr": {
        "title": "Politique de confidentialité",
        "updated": "Dernière mise à jour",
        "intro": "Cette politique explique quelles informations le jeu Whose Bag? (« le jeu ») utilise, pourquoi, et quels choix tu as. Le jeu est créé par {developer}, développeur indépendant (« je »).",
        "sections": [
            ("Ce que le jeu garde sur ton appareil", [
                "Ta progression, tes pièces, tes réglages (son, langue) et le fait d’avoir acheté « Supprimer les pubs » sont enregistrés uniquement sur ton appareil et ne me sont pas envoyés. Le jeu n’a pas de compte et ne demande jamais ton nom, ton adresse e-mail ni d’autres coordonnées.",
            ]),
            ("Publicité (Google AdMob)", [
                "Le jeu affiche des publicités via Google AdMob, un service de Google. Pour afficher et mesurer les publicités et lutter contre la fraude, Google peut collecter : l’identifiant publicitaire de ton appareil (sur iOS, seulement si tu autorises le suivi), ton adresse IP, des informations sur l’appareil et l’app comme le modèle, le système d’exploitation et la langue, une localisation approximative déduite de ton IP, et tes interactions avec les publicités.",
                "Là où la loi l’exige (Espace économique européen, Royaume-Uni et Suisse), les publicités personnalisées ne sont affichées qu’avec ton consentement ; sans lui, Google affiche des publicités non personnalisées. L’utilisation de ces informations par Google est expliquée sur {google_partners} et dans la {google_privacy_link}.",
            ]),
            ("Tes choix", [
                "Si tu te trouves dans l’EEE, au Royaume-Uni ou en Suisse, le jeu te demande ton consentement au premier lancement. Tu peux modifier ta réponse à tout moment dans le jeu : Réglages → Choix de confidentialité des pubs.",
                "Sur iPhone et iPad, iOS te demande si le jeu peut te suivre. Tu peux modifier ce choix à tout moment dans les Réglages de l’appareil → Confidentialité et sécurité → Suivi. Tu peux aussi réinitialiser ton identifiant publicitaire dans les réglages de l’appareil.",
                "Acheter « Supprimer les pubs » arrête les publicités entre les niveaux. Les publicités récompensées, que tu choisis de regarder pour un indice ou du temps en plus, restent disponibles.",
            ]),
            ("Achats intégrés", [
                "Les achats se font sur l’App Store et sont traités par Apple ; je ne reçois jamais tes informations de paiement. Le jeu utilise Unity In-App Purchasing, de Unity Technologies, pour communiquer avec l’App Store ; il vérifie tes achats sur ton appareil. Voir la {apple_privacy_link} et la {unity_privacy_link}.",
            ]),
            ("Enfants", [
                "Le jeu ne s’adresse pas aux enfants de moins de 13 ans, et je ne collecte pas sciemment d’informations personnelles les concernant.",
            ]),
            ("Conservation et suppression", [
                "Supprimer le jeu supprime tout ce qu’il a enregistré sur ton appareil. Les informations collectées par Google sont conservées et supprimées selon la politique de Google.",
            ]),
            ("Modifications", [
                "Si cette politique change, la nouvelle version sera publiée sur cette page avec une nouvelle date.",
            ]),
            ("Contact", [
                "Questions sur la confidentialité : {email}",
            ]),
        ],
        "google_privacy": "Politique de confidentialité de Google",
        "apple_privacy": "Politique de confidentialité d’Apple",
        "unity_privacy": "Politique de confidentialité de Unity",
    },
}

STYLE = """
:root { --bg: #f7f4ee; --ink: #1f2430; --muted: #5c6370; --rule: #e2ddd3; --accent: #c2410c; --card: #ffffff; }
@media (prefers-color-scheme: dark) { :root { --bg: #15171c; --ink: #eceae5; --muted: #a3a8b3; --rule: #2a2e36; --accent: #fb923c; --card: #1c1f26; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 17px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
main { max-width: 720px; margin: 0 auto; padding: 32px 20px 64px; }
nav { display: flex; flex-wrap: wrap; gap: 6px 14px; font-size: 14px; margin-bottom: 28px; }
nav a, nav span { color: var(--muted); text-decoration: none; }
nav span { color: var(--ink); font-weight: 600; }
nav a:hover { color: var(--accent); }
.game { font-size: 14px; letter-spacing: .08em; text-transform: uppercase; color: var(--accent); font-weight: 700; margin: 0; }
h1 { font-size: 32px; line-height: 1.2; margin: 6px 0 4px; }
.date { color: var(--muted); font-size: 14px; margin: 0 0 24px; }
h2 { font-size: 19px; margin: 32px 0 8px; padding-top: 20px; border-top: 1px solid var(--rule); }
p { margin: 0 0 12px; }
a { color: var(--accent); overflow-wrap: anywhere; }
footer { margin-top: 40px; color: var(--muted); font-size: 14px; }
"""


def page(lang_attr, title, body):
    return f"""<!doctype html>
<html lang="{lang_attr}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{STYLE}</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def link(url, text=None):
    return f'<a href="{url}">{html.escape(text or url)}</a>'


def policy(code):
    t = P[code]
    fill = {
        "developer": html.escape(DEVELOPER),
        "email": link("mailto:" + EMAIL, EMAIL),
        "google_partners": link(GOOGLE_PARTNERS),
        "google_privacy_link": link(GOOGLE_PRIVACY, t["google_privacy"]),
        "apple_privacy_link": link(APPLE_PRIVACY, t["apple_privacy"]),
        "unity_privacy_link": link(UNITY_PRIVACY, t["unity_privacy"]),
    }
    depth = "../" if code != "en" else ""
    nav = " ".join(
        f"<span>{name}</span>" if c == code else f'<a href="{depth}{"" if c == "en" else c + "/"}" hreflang="{HTML_LANG[c]}">{name}</a>'
        for c, name in LANGS)
    parts = [f"<nav>{nav}</nav>", '<p class="game">Whose Bag?</p>', f"<h1>{html.escape(t['title'])}</h1>",
             f'<p class="date">{t["updated"]}: {UPDATED[code]}</p>', f"<p>{html.escape(t['intro']).replace(html.escape('{developer}'), fill['developer'])}</p>"]
    for heading, paragraphs in t["sections"]:
        parts.append(f"<h2>{html.escape(heading)}</h2>")
        for text in paragraphs:
            escaped = html.escape(text)
            for key, value in fill.items():
                escaped = escaped.replace("{" + key + "}", value)
            parts.append(f"<p>{escaped}</p>")
    parts.append(f'<footer>© 2026 {html.escape(DEVELOPER)}</footer>')
    return page(HTML_LANG[code], f"{t['title']} · Whose Bag?", "\n".join(parts))


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    for code, _ in LANGS:
        write(f"whose-bag/privacy/{'' if code == 'en' else code + '/'}index.html", policy(code))
    home = "\n".join([
        f"<h1>{html.escape(DEVELOPER)}</h1>",
        "<p>Independent mobile games.</p>",
        "<h2>Whose Bag?</h2>",
        "<p>Pack a passenger’s suitcase before the flight leaves, then guess whose bag it is.</p>",
        f'<p>{link("whose-bag/privacy/", "Privacy Policy")}</p>',
        f'<footer>{link("mailto:" + EMAIL, EMAIL)}</footer>',
    ])
    write("index.html", page("en", DEVELOPER, home))
    print("built: index.html + whose-bag/privacy in", len(LANGS), "languages")


if __name__ == "__main__":
    main()
