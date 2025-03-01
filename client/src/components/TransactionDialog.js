// src/components/TransactionDialog.js
import React, { useState } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  Typography,
  Box,
  CircularProgress
} from '@mui/material';
import { ArrowUpward as DepositIcon, ArrowDownward as WithdrawIcon } from '@mui/icons-material';

const TransactionDialog = ({
  open,
  onClose,
  type,
  onSubmit,
  processing
}) => {
  const [amount, setAmount] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = () => {
    // Validate amount
    const numAmount = parseFloat(amount);

    if (isNaN(numAmount) || numAmount <= 0) {
      setError('Please enter a valid positive amount');
      return;
    }

    onSubmit(numAmount);
  };

  const handleClose = () => {
    setAmount('');
    setError('');
    onClose();
  };

  const isDeposit = type === 'deposit';
  const title = isDeposit ? 'Deposit Funds' : 'Withdraw Funds';
  const Icon = isDeposit ? DepositIcon : WithdrawIcon;
  const color = isDeposit ? 'success.main' : 'primary.main';

  return (
    <Dialog
      open={open}
      onClose={processing ? undefined : handleClose}
      maxWidth="xs"
      fullWidth
    >
      <DialogTitle>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Icon sx={{ color }} />
          <Typography variant="h6">{title}</Typography>
        </Box>
      </DialogTitle>

      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          id="amount"
          label="Amount"
          type="number"
          fullWidth
          value={amount}
          onChange={(e) => {
            setAmount(e.target.value);
            setError('');
          }}
          placeholder="Enter amount"
          inputProps={{
            min: 0,
            step: 0.01,
            inputMode: 'decimal'
          }}
          error={!!error}
          helperText={error}
          disabled={processing}
        />
      </DialogContent>

      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button
          onClick={handleClose}
          color="inherit"
          disabled={processing}
        >
          Cancel
        </Button>
        <Button
          onClick={handleSubmit}
          variant="contained"
          color={isDeposit ? "success" : "primary"}
          disabled={!amount || processing}
          startIcon={processing && <CircularProgress size={18} color="inherit" />}
        >
          {processing ? 'Processing' : 'Confirm'}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default TransactionDialog;