using System;
using System.Collections.Generic;

namespace BizX.Game
{
    [Serializable]
    public sealed class StarterGrant
    {
        public string ItemId;
        public int Quantity;
    }

    /// <summary>Deterministic, idempotent starter entitlement contract.</summary>
    public sealed class StarterPackService
    {
        public IReadOnlyList<StarterGrant> Grants { get; } = new[]
        {
            new StarterGrant { ItemId = "starter_outfit", Quantity = 1 },
            new StarterGrant { ItemId = "starter_tool", Quantity = 1 },
            new StarterGrant { ItemId = "starter_vehicle_skin", Quantity = 1 },
            new StarterGrant { ItemId = "starter_map", Quantity = 1 },
            new StarterGrant { ItemId = "starter_supply", Quantity = 3 },
            new StarterGrant { ItemId = "starter_inventory", Quantity = 5 }
        };

        public bool ShouldGrant(bool alreadyClaimed) => !alreadyClaimed;
    }
}
