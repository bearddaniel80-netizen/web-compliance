export const navigationConfig = {
  label: "Main navigation",

  items: [
    {
      id: "home",
      label: "Home",
      href: "/",
    },
    {
      id: "feature",
      label: "Features",
      children: [
        {
          id: "cache",
          label: "Cache",
          href: "/feature/cache",
        },
        {
          id: "failfast",
          label: "Failfast",
          href: "/feature/failfast",
        },
        {
          id: "failfast-query",
          label: "Failfast Query",
          href: "/feature/failfast-query",
        },
        {
          id: "profile",
          label: "Profile",
          href: "/feature/profile",
        },
        {
          id: "retry",
          label: "Retry",
          href: "/feature/retry",
        },
      ]
    },
    {
      id: "format",
      label: "Formats",
      children: [
        {
          id: "github",
          label: "Github",
          href: "/format/github",
        },
        {
          id: "html",
          label: "HTML",
          href: "/format/html",
        },
        {
          id: "json",
          label: "JSON",
          href: "/format/json",
        },
        {
          id: "markdown",
          label: "Markdown",
          href: "/format/markdown",
        },
        {
          id: "pdf",
          label: "PDF",
          href: "/format/pdf",
        },
      ],
    },
  ],
};