import express from "express";
import cors from "cors";
import { forwardFastapi } from "./middleware/forewardFastapi.js";
import { upload, upload_to_fastapi } from "./utils/fastapi.js";

const app = express();

app.use(express.json());
app.use(cors());

/*
 * ==================================================
 * Dynamic Routes
 * ==================================================
 */
app.get(
  "/api/manifest/:filename",
  forwardFastapi(
    (req) => `/api/manifest/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/github/:filename",
  forwardFastapi(
    (req) => `/api/manifest/github/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/html/:filename",
  forwardFastapi(
    (req) => `/api/manifest/html/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/markdown/:filename",
  forwardFastapi(
    (req) => `/api/manifest/markdown/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/pdf/:filename",
  forwardFastapi(
    (req) => `/api/manifest/pdf/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/cache/:filename",
  forwardFastapi(
    (req) => `/api/manifest/cache/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/failfast/:filename",
  forwardFastapi(
    (req) => `/api/manifest/failfast/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/failfast/query/:filename",
  forwardFastapi(
    (req) => `/api/manifest/failfast/query/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/profile/:filename",
  forwardFastapi(
    (req) => `/api/manifest/profile/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/manifest/retry/:times/:filename",
  forwardFastapi(
    (req) => `/api/manifest/retry/${encodeURIComponent(req.params.times)}/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/:filename",
  forwardFastapi(
    (req) => `/api/suite/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/github/:filename",
  forwardFastapi(
    (req) => `/api/suite/github/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/html/:filename",
  forwardFastapi(
    (req) => `/api/suite/html/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/markdown/:filename",
  forwardFastapi(
    (req) => `/api/suite/markdown/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/pdf/:filename",
  forwardFastapi(
    (req) => `/api/suite/pdf/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/cache/:filename",
  forwardFastapi(
    (req) => `/api/suite/cache/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/failfast/:filename",
  forwardFastapi(
    (req) => `/api/suite/failfast/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/failfast/query/:filename",
  forwardFastapi(
    (req) => `/api/suite/failfast/query/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/profile/:filename",
  forwardFastapi(
    (req) => `/api/suite/profile/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/suite/retry/:times/:filename",
  forwardFastapi(
    (req) => `/api/suite/retry/${encodeURIComponent(req.params.times)}/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/:filename",
  forwardFastapi(
    (req) => `/api/tag/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/github/:filename",
  forwardFastapi(
    (req) => `/api/tag/github/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/html/:filename",
  forwardFastapi(
    (req) => `/api/tag/html/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/markdown/:filename",
  forwardFastapi(
    (req) => `/api/tag/markdown/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/pdf/:filename",
  forwardFastapi(
    (req) => `/api/tag/pdf/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/cache/:filename",
  forwardFastapi(
    (req) => `/api/tag/cache/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/failfast/:filename",
  forwardFastapi(
    (req) => `/api/tag/failfast/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/failfast/query/:filename",
  forwardFastapi(
    (req) => `/api/tag/failfast/query/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/profile/:filename",
  forwardFastapi(
    (req) => `/api/tag/profile/${encodeURIComponent(req.params.filename)}`
  )
);
app.get(
  "/api/tag/retry/:times/:filename",
  forwardFastapi(
    (req) => `/api/tag/retry/${encodeURIComponent(req.params.times)}/${encodeURIComponent(req.params.filename)}`
  )
);
/*
 * ==================================================
 * Static Routes
 * ==================================================
 */
app.get("/api/data",
  forwardFastapi("/api/data")
);

// gets README from compliance cli
app.get("/api/index",
  forwardFastapi("/api/index")
);

app.get("/api/manifest/list",
  forwardFastapi("/api/manifest/list")
);

app.get("/api/suite/list",
  forwardFastapi("/api/suite/list")
);

app.get("/api/tag/list",
  forwardFastapi("/api/tag/list")
);

app.post("/api/uploads",   upload.single("file"),
  async (req, res) => {
    try {
      if (!req.file) {
        return res.status(400).json({
          error: "No file uploaded",
        });
      }

      const result = await upload_to_fastapi(
        "/api/uploads",
        req.file,
        {
          description: req.body.description,
        }
      );

      res
        .status(result.status)
        .json(result.data);

    } catch (error) {
      console.error("Upload failed:", error);

      res.status(500).json({
        error: "Upload failed",
      });
    }
  }
);
app.listen(4000, "0.0.0.0", () => {
  console.log("Server listening on port 4000");
});