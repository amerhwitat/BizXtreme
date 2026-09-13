package io.amerhwitat.bizx.mobile

data class MobileGameState(
    val mode: String = "default",
    val cash: Long = 10_000,
    val level: Int = 1,
    val score: Long = 0,
    val bizVirtual: Boolean = true,
    val network: String = "offline"
)

object MobileGameEngine {
    fun start(mode: String = "default", cash: Long = 10_000) = MobileGameState(mode, cash)
}
