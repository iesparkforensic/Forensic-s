# PVR Cinemas — Pending Bookings Workbook

`PVR_Pending_Bookings.xlsx` collects bookings **111121 onwards** with their status
(Pending / Cancelled / Paid / Open) and core show details.

## Workbook structure

- **All Bookings** — master data-entry sheet. One booking per row starting at row 5.
  Row 4 is a greyed **example** row (delete before use). Column **Status** has a
  dropdown: `Pending`, `Cancelled`, `Paid`, `Open`.
- **Pending / Cancelled / Paid / Open** — one tab per status, populated from the
  master sheet once source data is loaded.

### Columns (Core details)

| Column | Notes |
|---|---|
| Booking ID | e.g. `111121` |
| Status | Pending / Cancelled / Paid / Open |
| Movie | title + format (2D/3D/IMAX) |
| Cinema / Screen | property + audi/screen |
| Show Date & Time | `YYYY-MM-DD HH:MM` |
| Seats | e.g. `H12, H13, H14` |
| Seat Count | number of seats |

## Supplying the data

The PVR `unpaid-to-paid` screen is behind login + Akamai, so the data has to be
captured from a browser already signed in. Any one of these works:

1. **Built-in export** — if the screen has an *Export to Excel/CSV*, share that file.
2. **Network capture** — F12 → Network → Fetch/XHR → reload → copy the booking
   request's **URL** and **JSON response**. From one sample, a console script can
   loop `111121 → N` and download the full set under your own session.

Once the raw data is provided, the master sheet and status tabs are filled from it.
