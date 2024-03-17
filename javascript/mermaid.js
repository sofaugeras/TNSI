




<!DOCTYPE html>
<html class="gl-light ui-neutral with-header with-top-bar " lang="fr">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>docs/javascripts/mermaid.js · master · GiYoM / ECS1 · GitLab</title>
<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"explainCodeChat":false};gon.licensed_features={"remoteDevelopment":true};
//]]>
</script>

<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: String!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: [$filePath], ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"GiYoM/ecs1","ref":"master","refType":"","filePath":"docs/javascripts/mermaid.js","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"QMPBgbz5Acx5x69MWLxtVWeMhg1m1nRVZGWx6BEsNklXDY_NwkW9XC4K9kUX9d3CzMaC8KyHjkWN5WHC5HaMPQ","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.f14e6e18.chunk.js">

<link rel="stylesheet" href="/assets/application-58ebcd8f96ecc2ebf7f29122395e38ee28dc833dfc6d08fb667d2655da971df6.css" media="all" />
<link rel="stylesheet" href="/assets/page_bundles/tree-b4f64ab3e002724dc28b8becb5d4779ebe6b018d25d71b614bfe91c6eaefb462.css" media="all" /><link rel="stylesheet" href="/assets/page_bundles/projects-5d82d7ca1c2c0f93b4c32b9a1830a86773594d265a72c1a696ea16ff43a7ee32.css" media="all" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-b1dab9b10010cbb9c3738689b18ce46a4f58b98a8d483226fdff8a776a45caf0.css" media="all" />
<link rel="stylesheet" href="/assets/application_utilities-92001ae3073c6aa1cc412e6bdfe1028a260e3540a81cb767eeab6fe75ff704c4.css" media="all" />
<link rel="stylesheet" href="/assets/tailwind-ca5c6bf6eedbe0332255b96f7309b76b80e1ec59a3d4871d37388833910feacc.css" media="all" />


<link rel="stylesheet" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" media="all" />
<link rel="stylesheet" href="/assets/highlight/themes/white-ea2e64b41e475880325eb5dea8d116c1bb15d3548331fbcffaaf0276b0329aa9.css" media="all" />

<script src="/assets/webpack/runtime.0981333c.bundle.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/main.02e3a706.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/tracker.93da9d74.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/analytics.9bd582a3.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"snowplow.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-0-9","data":{"environment":"production","source":"gitlab-rails","plan":"free","extra":{},"user_id":null,"is_gitlab_team_member":null,"namespace_id":4039297,"project_id":19386387,"context_generated_at":"2024-03-17T21:19:07.362Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace4039297/project19386387/-/blob/:repository_path";


//]]>
</script>
<link rel="preload" href="/assets/application_utilities-92001ae3073c6aa1cc412e6bdfe1028a260e3540a81cb767eeab6fe75ff704c4.css" as="style" type="text/css" nonce="0YCQgMxK0hDR4JR+rik7wg==">
<link rel="preload" href="/assets/application-58ebcd8f96ecc2ebf7f29122395e38ee28dc833dfc6d08fb667d2655da971df6.css" as="style" type="text/css" nonce="0YCQgMxK0hDR4JR+rik7wg==">
<link rel="preload" href="/assets/highlight/themes/white-ea2e64b41e475880325eb5dea8d116c1bb15d3548331fbcffaaf0276b0329aa9.css" as="style" type="text/css" nonce="0YCQgMxK0hDR4JR+rik7wg==">
<link crossorigin="" href="https://snowplow.trx.gitlab.net" rel="preconnect">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-1e0a5107ea3bbd4be93e8ad2c503467e43166cd37e4293570b490e0812ede98b.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-Italic-38eaf1a569a54ab28c58b92a4a8de3afb96b6ebc250cf372003a7b38151848cc.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-08d2c5e8ff8fd3d2d6ec55bc7713380f8981c35f9d2df14e12b835464d6e8f23.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-Italic-38e58d8df29485a20c550da1d0111e2c2169f6dcbcf894f2cd3afbdd97bcc588.woff2" rel="preload">
<link rel="preload" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" as="style" type="text/css" nonce="0YCQgMxK0hDR4JR+rik7wg==">

<script src="/assets/locale/fr/app-5d1f63947764801c29274332af4742e22de9f24d4d44da5cc4964ea4625fdc68.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>

<script src="/assets/webpack/sentry.f8cc36b9.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>


<script src="/assets/webpack/commons-pages.search.show-super_sidebar.8653df83.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/super_sidebar.7a25ac7c.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.groups-pages.groups.achievements-pages.groups.activity-pages.groups.analytics.ci_cd_an-83cc6c04.dac29807.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.admin.runners.show-pages.clusters.agents.dashboard-pages.explore.catalog-pages.groups.-db6831ac.65d4090f.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.groups.security.policies.edit-pages.groups.security.policies.new-pages.projects.blob.s-c8e0a3ae.f6952603.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.admin.subscriptions.show-pages.groups.security.policies.edit-pages.groups.security.pol-6bfecbfa.31f430b9.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/109.b8ef2857.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.groups.show-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show--90d3b3a3.27414c4e.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.dd9b4f24.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blame.streaming-pages.projects.blob.show-pages.proj-9f3d272f.ec37068a.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/164.43f945c6.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.24ad1a1b.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.commits.show-pages.projects.compare.show.5ff2b541.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show.f68f5ad1.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<script src="/assets/webpack/pages.projects.blob.show.a74d2dba.chunk.js" defer="defer" nonce="TWITOj5nk2ETOCPCOwBNvw=="></script>
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="docs/javascripts/mermaid.js · master · GiYoM / ECS1 · GitLab" property="og:title">
<meta content="Mathématiques en ECS1 à l&#39;Externat" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/GiYoM/ecs1/-/blob/master/docs/javascripts/mermaid.js" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="docs/javascripts/mermaid.js · master · GiYoM / ECS1 · GitLab" property="twitter:title">
<meta content="Mathématiques en ECS1 à l&#39;Externat" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="AUfKbJ3cwqjVfHxBSKw74LQ_kTFSrDZaMXTGwxnfryAWiYQg42B-OIKxJUgH5Yt3H3WVzJj9zErY9Bbp7IUVVA" />
<meta name="csp-nonce" content="TWITOj5nk2ETOCPCOwBNvw==" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="Mathématiques en ECS1 à l&#39;Externat" name="description">
<meta content="#ececef" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-firefox gl-platform-windows  " data-find-file="/GiYoM/ecs1/-/find_file/master" data-namespace-id="4039297" data-page="projects:blob:show" data-page-type-id="master/docs/javascripts/mermaid.js" data-project="ecs1" data-project-id="19386387">

<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isFirefox":true,"isWindows":true};


//]]>
</script>



<header class="header-logged-out" data-testid="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<nav aria-label="Explorer GitLab" class="header-logged-out-nav gl-display-flex gl-gap-3 gl-justify-content-space-between">
<div class="gl-display-flex gl-align-items-center gl-gap-1">
<span class="gl-sr-only">GitLab</span>
<a title="Page d&#39;accueil" id="logo" class="header-logged-out-logo has-tooltip" aria-label="Page d&#39;accueil" data-track-label="main_navigation" data-track-action="click_gitlab_logo_link" data-track-property="navigation_top" href="/"><svg aria-hidden="true" role="img" class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#E24329"/>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#FC6D26"/>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z"
        fill="#FCA326"/>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z"
        fill="#FC6D26"/>
</svg>

</a></div>
<ul class="gl-list-style-none gl-p-0 gl-m-0 gl-display-flex gl-gap-3 gl-align-items-center gl-flex-grow-1">
<li class="header-logged-out-nav-item header-logged-out-dropdown gl-md-display-none">
<button class="header-logged-out-toggle" data-toggle="dropdown" type="button">
<span class="gl-sr-only">
Menu
</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-4063a836235237e06f94879673f65492fe427d05e26482ddbde40ad6d227a3f8.svg#hamburger"></use></svg>
</button>
<div class="dropdown-menu">
<ul>
<li>
<a href="https://about.gitlab.com/why-gitlab">Les raisons de choisir GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/pricing">Tarification
</a></li>
<li>
<a href="https://about.gitlab.com/sales">Contacter le service commercial
</a></li>
<li>
<a href="/explore">Explorer</a>
</li>
</ul>
</div>
</li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/why-gitlab">Les raisons de choisir GitLab
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/pricing">Tarification
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/sales">Contacter le service commercial
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a class="" href="/explore">Explorer</a>
</li>
</ul>
<ul class="gl-list-style-none gl-p-0 gl-m-0 gl-display-flex gl-gap-3 gl-align-items-center gl-justify-content-end">
<li class="header-logged-out-nav-item">
<a href="/users/sign_in?redirect_to_referer=yes">Connexion</a>
</li>
<li class="header-logged-out-nav-item">
<a class="gl-button btn btn-md btn-confirm " href="/users/sign_up"><span class="gl-button-text">
Essai gratuit

</span>

</a></li>
</ul>
</nav>
</div>
</header>

<div class="layout-page page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/GiYoM/ecs1/-/files/master?format=json&quot;,&quot;project_blob_url&quot;:&quot;/GiYoM/ecs1/-/blob/master&quot;}" data-force-desktop-expanded-sidebar="" data-root-path="/" data-sidebar="{&quot;is_logged_in&quot;:false,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Explorer&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;ECS1&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:19386387,&quot;link&quot;:&quot;/GiYoM/ecs1&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Gestion&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/activity&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activité&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/activity&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Membres&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/project_members&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/labels&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Programmation&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/issues&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Tickets&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/issues&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Tableaux des tickets&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/boards&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Jalons&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/milestones&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/wikis/home&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Requêtes de fusion&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/merge_requests&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Dépôt&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/tree/master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/branches&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Validations&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/commits/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Étiquettes&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/tags&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Graphe du dépôt&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/network/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Comparer les révisions&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/compare?from=master\u0026to=master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Extraits de code&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/snippets&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Compilation&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/pipelines&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/jobs&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Planifications de pipeline&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/pipeline_schedules&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artéfacts&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/artifacts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Déploiement&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/releases&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/releases&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Registre de paquets&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/packages&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Registre de conteneur&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/container_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/ml/models&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Opération&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/environments&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environnements&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/environments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Modules Terraform&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/infrastructure_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Surveillance&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/incidents&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/incidents&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;service_desk&quot;,&quot;title&quot;:&quot;Service d&#39;assistance&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/issues/service_desk&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyse&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Données d&#39;analyse des chaînes de valeur&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/value_stream_analytics&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/graphs/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;Données d&#39;analyse CI/CD&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/pipelines/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Données d&#39;analyse du dépôt&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/graphs/master/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Expériences du modèle&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/GiYoM/ecs1/-/ml/experiments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:&quot;Projet&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;display_whats_new&quot;:true,&quot;whats_new_most_recent_release_items_count&quot;:7,&quot;whats_new_version_digest&quot;:&quot;0e2cba433c3aeb69ca7ff586375ef7f37449a9e5354ceaff182fc964b4808266&quot;,&quot;show_version_check&quot;:null,&quot;gitlab_version&quot;:{&quot;major&quot;:16,&quot;minor&quot;:10,&quot;patch&quot;:0,&quot;suffix_s&quot;:&quot;&quot;},&quot;gitlab_version_check&quot;:null,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:19386387,&quot;name&quot;:&quot;ECS1&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/GiYoM/ecs1/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/GiYoM/ecs1/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;master&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Extraits de code&quot;,&quot;href&quot;:&quot;/explore/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Groupes&quot;,&quot;href&quot;:&quot;/explore/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projets&quot;,&quot;href&quot;:&quot;/explore/projects&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;}]}"></aside>

<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">

























<div class="top-bar-fixed container-fluid" data-testid="top-bar">
<div class="top-bar-container gl-display-flex gl-align-items-center gl-gap-2">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle gl-ml-n3" aria-controls="super-sidebar" aria-expanded="false" aria-label="Barre latérale de navigation principale" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-4063a836235237e06f94879673f65492fe427d05e26482ddbde40ad6d227a3f8.svg#sidebar"></use></svg>

</button>
<nav aria-label="Fil d&#39;Ariane" class="breadcrumbs gl-breadcrumbs" data-testid="breadcrumb-links">
<ul class="breadcrumb gl-breadcrumb-list js-breadcrumbs-list">
<li class="gl-breadcrumb-item gl-display-inline-flex"><a href="/GiYoM">GiYoM</a></li> <li class="gl-breadcrumb-item gl-display-inline-flex"><a class="gl-display-inline-flex!" href="/GiYoM/ecs1"><span class="js-breadcrumb-item-text">ECS1</span></a></li>

<li class="gl-breadcrumb-item" data-testid="breadcrumb-current-link">
<a href="/GiYoM/ecs1/-/blob/master/docs/javascripts/mermaid.js">Dépôt</a>
</li>
</ul>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"GiYoM","item":"https://gitlab.com/GiYoM"},{"@type":"ListItem","position":2,"name":"ECS1","item":"https://gitlab.com/GiYoM/ecs1"},{"@type":"ListItem","position":3,"name":"Dépôt","item":"https://gitlab.com/GiYoM/ecs1/-/blob/master/docs/javascripts/mermaid.js"}]}

</script>
</nav>



</div>
</div>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>




<div class="js-signature-container" data-signatures-path="/GiYoM/ecs1/-/commits/9b98bb2fe362733e73f516b04c16b158c29e7f15/signatures?limit=1"></div>

<div class="tree-holder gl-pt-4" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder gl-max-w-26">
<div data-project-id="19386387" data-project-root-path="/GiYoM/ecs1" data-ref="master" data-ref-type="" id="js-tree-ref-switcher"></div>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/GiYoM/ecs1/-/tree/master">ecs1
</a></li>
<li class="breadcrumb-item">
<a href="/GiYoM/ecs1/-/tree/master/docs">docs</a>
</li>
<li class="breadcrumb-item">
<a href="/GiYoM/ecs1/-/tree/master/docs/javascripts">javascripts</a>
</li>
<li class="breadcrumb-item">
<a href="/GiYoM/ecs1/-/blob/master/docs/javascripts/mermaid.js"><strong>mermaid.js</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-display-flex gl-flex-wrap gl-sm-flex-nowrap gl-align-items-baseline gl-gap-3">
<a aria-keyshortcuts="t" class="gl-button btn btn-md btn-default has-tooltip shortcuts-find-file" data-html="true" title="Accéder à la recherche de fichier &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;t&lt;/kbd&gt;" rel="nofollow" href="/GiYoM/ecs1/-/find_file/master"><span class="gl-button-text">
Rechercher un fichier
</span>

</a>

<a class="gl-button btn btn-md btn-default js-blob-blame-link" href="/GiYoM/ecs1/-/blame/master/docs/javascripts/mermaid.js"><span class="gl-button-text">
Blame
</span>

</a>
<a class="gl-button btn btn-md btn-default " href="/GiYoM/ecs1/-/commits/master/docs/javascripts/mermaid.js"><span class="gl-button-text">
Historique
</span>

</a>
<a aria-keyshortcuts="y" class="gl-button btn btn-md btn-default has-tooltip js-data-file-blob-permalink-url" data-html="true" title="Go to permalink &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;y&lt;/kbd&gt;" href="/GiYoM/ecs1/-/blob/9448ac94bcebb8a36aa0bfe6d26d0208ffa92a41/docs/javascripts/mermaid.js"><span class="gl-button-text">
Lien permanent
</span>

</a>
</div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-9b98bb2f">
<div class="avatar-cell d-none d-sm-block">
<a href="/GiYoM"><img alt="GiYoM&#39;s avatar" src="/uploads/-/system/user/avatar/3142426/avatar.png?width=40" class="avatar s40 gl-display-none gl-sm-display-inline-block" title="GiYoM"></a>
</div>
<div class="commit-detail flex-list gl-display-flex gl-justify-content-space-between gl-align-items-center gl-flex-grow-1 gl-min-w-0">
<div class="commit-content" data-testid="commit-content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/GiYoM/ecs1/-/commit/9b98bb2fe362733e73f516b04c16b158c29e7f15">update</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
9b98bb2f
</span>
<div class="committer">
<a class="commit-author-link js-user-link" data-user-id="3142426" href="/GiYoM">GiYoM</a> a rédigé <time class="js-timeago" title="mai 2, 2021 6:17pm" datetime="2021-05-02T18:17:39Z" data-toggle="tooltip" data-placement="bottom" data-container="body">mai 02, 2021</time>
</div>

</div>
<div class="commit-actions flex-row">

<a class="gl-badge badge badge-pill badge-success md ci-icon ci-icon-variant-success gl-p-2 gl-ml-3" data-container="body" data-placement="left" data-testid="ci-icon" data-toggle="tooltip" href="/GiYoM/ecs1/-/commit/9b98bb2fe362733e73f516b04c16b158c29e7f15/pipelines?ref=master" title="Pipeline: réussi"><span class="js-ci-status-badge-legacy ci-icon-gl-icon-wrapper"><svg class="s24 gl-icon" data-testid="status_success_borderless-icon"><use href="/assets/icons-4063a836235237e06f94879673f65492fe427d05e26482ddbde40ad6d227a3f8.svg#status_success_borderless"></use></svg></span></a>
<div class="js-commit-pipeline-status" data-endpoint="/GiYoM/ecs1/-/commit/9b98bb2fe362733e73f516b04c16b158c29e7f15/pipelines?ref=master"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
9b98bb2f
</div>
<button class="gl-button btn btn-icon btn-md btn-default " title="Copier le SHA de la validation" aria-label="Copier le SHA de la validation" aria-live="polite" data-toggle="tooltip" data-placement="bottom" data-container="body" data-html="true" data-category="primary" data-size="medium" data-clipboard-text="9b98bb2fe362733e73f516b04c16b158c29e7f15" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="copy-to-clipboard-icon"><use href="/assets/icons-4063a836235237e06f94879673f65492fe427d05e26482ddbde40ad6d227a3f8.svg#copy-to-clipboard"></use></svg>

</button>

</div>
</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="docs/javascripts/mermaid.js" data-explain-code-available="false" data-new-workspace-path="/-/remote_development/workspaces/new" data-original-branch="master" data-project-path="GiYoM/ecs1" data-ref-type="" data-resource-id="gid://gitlab/Project/19386387" data-target-branch="master" data-user-id="" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-label="Chargement en cours" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div>
</div>
</div>

</div>
<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/GiYoM/ecs1/edit/master/-/docs/javascripts/mermaid.js'


//]]>
</script>
<div data-ambiguous="false" data-ref="master" id="js-ambiguous-ref-modal"></div>

</main>
</div>


</div>
</div>


<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script nonce="TWITOj5nk2ETOCPCOwBNvw==">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

