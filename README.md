# Deskline — study stream companion

A single-file study-with-me timer: dashboard (settings, stats, break confirm,
sudden focus checks, to-do list) + a transparent overlay view for OBS,
kept in sync through Firebase Realtime Database.

## 1. Create a Firebase project (free)

1. Go to https://console.firebase.google.com → **Add project** → give it any name → finish setup.
2. In the project, click the **</> (Web)** icon to register a web app. You don't need Firebase Hosting — just the config.
3. Firebase will show you a config object like:
   ```js
   const firebaseConfig = {
     apiKey: "AIza...",
     authDomain: "your-project.firebaseapp.com",
     databaseURL: "https://your-project-default-rtdb.firebaseio.com",
     projectId: "your-project",
     ...
   };
   ```
4. In the left sidebar, go to **Build → Realtime Database → Create Database**. Pick any region, start in **test mode** for now (rules below tighten it).
5. In the Realtime Database **Rules** tab, paste:
   ```json
   {
     "rules": {
       "deskline": {
         "$room": {
           "state": {
             ".read": true,
             ".write": true
           }
         }
       }
     }
   }
   ```
   This scopes read/write to a per-room path so only someone who has your specific overlay link can see or change your data — it's not authenticated, so treat that link as private, not secret.

## 2. Add your config to the app

Open `index.html`, find this near the top of the `<script>` block:

```js
var FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT-default-rtdb.firebaseio.com",
  projectId: "YOUR_PROJECT"
};
```

Replace the four values with what Firebase gave you in step 1.3. Until this is filled in, the app still runs locally but shows a "Firebase isn't configured" banner and won't save or sync anything.

## 3. Deploy to GitHub Pages

```bash
git init
git add .
git commit -m "Deskline study stream app"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Then in the repo on GitHub: **Settings → Pages → Source: Deploy from branch → main → / (root)**. After a minute your app is live at:

```
https://<your-username>.github.io/<your-repo>/
```

## 4. Add the overlay to OBS

Open the deployed link, go to the **Overlay layout** tab, and copy the link shown there (it already includes your room ID and `?view=overview`). In OBS:

- **Sources → + → Browser Source**
- Paste the copied URL
- Width/height: something 16:9, e.g. 1920×1080
- Leave "Shutdown source when not visible" unchecked if you want the sudden-check flash to keep working while the scene isn't active

Your dashboard tab is the only place that controls the session and reads chat/inputs — the overlay is read-only and updates live as you use the dashboard.

## Notes

- Everyone who loads your dashboard link generates/keeps their own room ID (stored in the browser via `localStorage`), so you and, say, a friend testing the same deployed site won't collide.
- If you ever want this locked down further, add Firebase Authentication and update the rules to check `auth != null` — happy to help with that if you want it later.
