from __future__ import annotations

import AuroraMR as amr

if __name__ == "__main__":
    amr.play_motion_by_kind(
        "ackermann",
        interval_ms=28,
        playback_speed=0.5,
        show=True,
        log=True,
        log_every_n_frames=10,
        log_detailed=False,
    )
