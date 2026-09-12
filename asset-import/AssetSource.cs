using System;

namespace BizXtreme.AssetImport
{
    public sealed class AssetSource
    {
        public string Url { get; init; } = "";
        public string License { get; init; } = "";
        public string Attribution { get; init; } = "";
        public string Format { get; init; } = "";
        public bool AllowsDownload { get; init; }
        public bool AllowsReuse { get; init; }
        public string Sha256 { get; init; } = "";

        public bool IsImportable => AllowsDownload && AllowsReuse && Uri.TryCreate(Url, UriKind.Absolute, out _);
    }
}
